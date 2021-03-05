     


/*****************************************************************************************
 * 
 *                                  Utility functions
 * 
 *****************************************************************************************/

/**
 * Distance between two points p1 and p2
 */
const getDistance = (p1, p2 = {x:0,y:0}) => Math.sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y));
/**
 * Comptute vector v such that OP1 + v = OP2 
 */
const getTranslator = (p1, p2 = {x:0,y:0}) => ({deltaX: p2.x - p1.x, deltaY: p2.y - p1.y});
/**
 * Comptute vector v such that OP1 + OP2 = v 
 */
const sumCoords = (p1, p2) => ({x: p1.x + p2.x, y: p1.y + p2.y})
/**
 * Comptute vector v such that k * OP1 = v where k is a scalar (aka scalar multiplication)
 */
const scalarByCoords = (p1, k) => ({x: k * p1.x, y: k * p1.y})
/**
 * Compute new rectangle with same dimensions but translated i.e. its upper left corner coordinate are translated by {deltaX, deltaY}
 */
const applyTranslatorToRect = ({x, y, width, height}, { deltaX, deltaY }) => ({x: x + deltaX, y: y + deltaY, width, height});
/**
 * Set left and top style properies of node to x and y effectively moving the node to the coordinates {x,y}
 */
const moveNodeToCoords = (node, { x, y }) => ((node.style.left = `${x}px`) && (node.style.top = `${y}px`));
/**
 * Instead of moving node to the coordinates {x,y}, set css variables to hold these values. 
 * The node can then be moved at some later point by dynamically manipulating css classes.
 */
const putCoordsOnNode = (node, { x, y }) => { node.style.setProperty('--to-x', `${x}px`); node.style.setProperty('--to-y', `${y}px`);};
/**
 * Convert cartesian coordinates {x,y} to polar coordinates {r, theta}
 */
const cartesian2Polar = ({x, y}) => ({ distance: getDistance({x, y}), radians: Math.atan2(y, x) })
/**
 * Convert polar coordinates {r, theta} to polar cartesian {x,y}
 */
const polar2Cartesian = ({distance, radians}) => ({ x: distance * Math.cos(radians), y: distance * Math.sin(radians) });
/**
 * Given a vector OP in cartesian coordinates {x,y} rotate the angle by an angle 'radiansAngle'
 * Where P is the "point" input argument
 */
const rotatePoint = (point, radiansAngle) => {
    const {distance, radians} = cartesian2Polar(point);
    return polar2Cartesian({distance, radians: radians + radiansAngle});
}



/**
 * A point "P" is looking a circle with center "C". How much angle does the circle occupy at this distance?
 * ```
 *  - OT1 = OC + a/d  CP + b/d x CPperpendicular 
 *  - OT2 = OC + a/d  CP - b/d x CPperpendicular
 * ``` 
 *  - where 
 *    - T1 and T2 are tangent points on the circle
 *    - CP (center of circle to P) has a length d
 *    - CPperpendicular is CP rotated by 90 degrees clock
 *    - The equations express CP using its components along CP (length a) and CPperpendicular (length b)
 * 
 * https://math.stackexchange.com/questions/543496/how-to-find-the-equation-of-a-line-tangent-to-a-circle-that-passes-through-a-g
 */
const getViewingAngle = (viewPoint, targetCircle) => {


    const { center: targetCenter, radius: targetRadius } = targetCircle;
    const distance = getDistance(viewPoint, targetCenter);
    if(distance < targetRadius) throw new Error(`Point with cordinates (${viewPoint.x}, ${viewPoint.y}) is within the circle and cannot be used to generate tangents lines`);

    // Compute vector CP and CP rotated by 90 degrees
    const {deltaX: deltaXParallel, deltaY: deltaYParallel} = getTranslator(targetCenter, viewPoint); // CP x,y components
    const deltaXPerpendicular = -1 * deltaYParallel; // CP rotated x,y components
    const deltaYPerpendicular = deltaXParallel;
    
    // Compute intermediary values for final calculations
    const { x: cx, y: cy } = targetCenter;
    const rho = targetRadius / distance;
    const a_d = rho * rho;
    const b_d = rho * Math.sqrt(1 - rho * rho);

    // Compute x,y components of OT1 and OT2 where O is the origin of the coordinate system (0,0)
    // a_d = a/d where d is the distance of CP: CT1x = a_d x CP
    // b_d = b/d where d is the distance of CP: CT1y = b_d x CProtated
    // a is therefore the projection of CT along CP
    // b is therefore the projection of CT along a direction perpendicular to CP
    const T1x = cx + a_d * deltaXParallel + b_d * deltaXPerpendicular;
    const T1y = cy + a_d * deltaYParallel + b_d * deltaYPerpendicular;
    const T2x = cx + a_d * deltaXParallel - b_d * deltaXPerpendicular;
    const T2y = cy + a_d * deltaYParallel - b_d * deltaYPerpendicular;
    
    // Assert that the tangents points computed are actually on the circle's circumference
    if(Math.round(getDistance(targetCenter, {x: T1x, y: T1y}) - targetRadius) !== 0) throw new Error("Tangent point does not lie on circumference");
    if(Math.round(getDistance(targetCenter, {x: T2x, y: T2y}) - targetRadius) !== 0) throw new Error("Tangent point does not lie on circumference");


    // Compute the angle theta = (T1, P, T2) which is the viewing angle of the circle observed from P the viewpoint
    // a.b = |a| . |b| . cos(theta)   (Scalar Multiplication)
    const angle = Math.acos((
            (T1x - viewPoint.x)*(T2x - viewPoint.x) + (T1y - viewPoint.y)*(T2y - viewPoint.y)
        )/(
            getDistance(viewPoint, {x:T1x, y:T1y}) * getDistance(viewPoint, {x:T2x, y:T2y})
        )
    );

    return {
        angle: angle,
        tangents: [ { x: T1x, y: T1y }, { x: T2x, y: T2y } ]
    }  
}

/**
 * Get the circle that either fits inside the rectangle, or the circle that contains the rectangle.
 */
const getCircleFromRect = ({x, y, width, height})=>{
    const center = { x: x + width / 2, y: y + height / 2 };
    const radius = getDistance(center, {x, y});
    if(Math.round(getDistance(center, {x, y}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    if(Math.round(getDistance(center, {x:x+width, y:y}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    if(Math.round(getDistance(center, {x:x+width, y:y+height}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    if(Math.round(getDistance(center, {x, y:y+height}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    return {center, radius: Math.min(width / 2, height / 2)}
}

/**
 * A point is looking at a bunch of circles. How much cumulative angle do they occupy?
 */
const getAngleFromCircles = (viewPoint, circles, maxAngle = Math.PI) => {
    const angle = circles.reduce((acc, circle) => acc + getViewingAngle(viewPoint, circle).angle, 0);
    if(angle >= maxAngle) throw new Error("Circles do not fit at current distance from viewpoint");
    return angle; 
}




/**
 * The menu tries to arrange the nav items around itself so that they all fit within te angle "maxAngle"
 * If they dont, push they away from the menu center by step pixel, and try again recursively
 */
function expandMenuCircle(menuCenter, navRects, step = 100, maxAngle = Math.PI){
    try {
        return {
            // getAngleFromCircles throws an error if the accumulated angle for all these circle is greater than maxAngle
            angle: getAngleFromCircles(menuCenter, navRects.map(rect => getCircleFromRect(rect)), maxAngle),
            rects: navRects
        }
    }catch(e){
        // On error thrown by getAngleFromCircles, push the circles a little bit further, and try again recursively
        return expandMenuCircle(menuCenter, navRects.map(rect => applyTranslatorToRect(rect, {deltaX: 0, deltaY: -1 * step})), step, maxAngle);
    }
}        





























/*****************************************************************************************
 * 
 *                                  Main Function
 * 
 *****************************************************************************************/

/**
 * Position nav items around a menu so that they fit within some angle.
 */
export default function positionMenuItem(){
    // Constants to regulate the positioning algorithm
    const angularSpace = Math.PI / 2;
    const angularAnchor = Math.PI;
    const menuExpansionSteps = 5; 

    // Node items involved
    const navs = Array.from(document.querySelectorAll(".nav__item"));
    const menu = document.querySelector(".hamburger-menu");

    // Get center point of menu 
    const {center: viewPoint, radius: viewPointSize} = getCircleFromRect(menu.getBoundingClientRect())
    // Try to compute a distance at which the nav items can nicely fit around the menu within an angle "angularSpace"
    const {angle, rects} = expandMenuCircle(viewPoint, navs.map(nav => nav.getBoundingClientRect()), menuExpansionSteps, angularSpace);
    // Compute the space between the nav items, so that they are nicely spread out to occupy the "angularSpace"
    const angleGap = angularSpace/(navs.length - 1);

    // Collect important points for display purposes
    const coordsArr = [{item: 'menu', radius: viewPointSize, ...viewPoint}];

    
    // Attempt to actually move the nav items
    // rects contain the distance information for where these items will sit
    rects.reduce((acc, rect, i)=> {
        // First get the circle related to the menu
        const circle = getCircleFromRect(rect);

        // Extract the distance
        const distance = getDistance(viewPoint, circle.center);

        // Compute the translation vector to move a nav item from the menu position to 
        // where it needs to sit so that they form a circle around the menu. Then put this information
        // on the node itself via css variables. Lastly collect this data for display purposes
        const coordsChange = polar2Cartesian({distance, radians: acc});
        putCoordsOnNode(navs[i], coordsChange);
        coordsArr.push({item: `nav${i}`, radius: circle.radius, ...coordsChange })
        
        // Prepare to position next nav item
        return acc + angleGap;

    // Initial angular position for first nav item 
    }, angularAnchor);


    console.log(coordsArr);
}

