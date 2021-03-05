     


/* Utility functions */
const getDistance = (p1, p2 = {x:0,y:0}) => Math.sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y));
const getTranslator = (p1, p2 = {x:0,y:0}) => ({deltaX: p2.x - p1.x, deltaY: p2.y - p1.y});
const applyTranslatorToRect = ({x, y, width, height}, { deltaX, deltaY }) => ({x: x + deltaX, y: y + deltaY, width, height});
const moveNodeToCoords = (node, { x, y }) => ((node.style.left = `${x}px`) && (node.style.top = `${y}px`));
const putCoordsOnNode = (node, { x, y }) => { node.style.setProperty('--to-x', `${x}px`); node.style.setProperty('--to-y', `${y}px`);};
const cartesian2Polar = ({x, y}) => ({ distance: getDistance({x, y}), radians: Math.atan2(y, x) })
const polar2Cartesian = ({distance, radians}) => ({ x: distance * Math.cos(radians), y: distance * Math.sin(radians) });
const sumCoords = (p1, p2) => ({x: p1.x + p2.x, y: p1.y + p2.y})
const scalarByCoords = (p1, k) => ({x: k * p1.x, y: k * p1.y})


const getViewingAngle = (viewPoint, targetCircle) => {
    // https://math.stackexchange.com/questions/543496/how-to-find-the-equation-of-a-line-tangent-to-a-circle-that-passes-through-a-g

    // OT1 = OC + a/d CP + b/d CPperpendicular
    // OT2 = OC + a/d CP - b/d CPperpendicular
    // where 
    //     T1 and T2 are tangent points on the circle
    //     CP (center to P) has a length d
    //     CPperpendicular is CP rotated by 90 degrees clock
    //     The equations express CP using its components along CP (length a) and CPperpendicular (length b)

    const { center: targetCenter, radius: targetRadius } = targetCircle;
    const distance = getDistance(viewPoint, targetCenter);
    if(distance < targetRadius) throw new Error(`Point with cordinates (${viewPoint.x}, ${viewPoint.y}) is within the circle and cannot be used to generate tangents lines`);


    const {deltaX: deltaXParallel, deltaY: deltaYParallel} = getTranslator(targetCenter, viewPoint);
    const deltaXPerpendicular = -1 * deltaYParallel;
    const deltaYPerpendicular = deltaXParallel;
    

    const { x: cx, y: cy } = targetCenter;
    const rho = targetRadius / distance;
    const a_d = rho * rho;
    const b_d = rho * Math.sqrt(1 - rho * rho);

    const T1x = cx + a_d * deltaXParallel + b_d * deltaXPerpendicular;
    const T1y = cy + a_d * deltaYParallel + b_d * deltaYPerpendicular;
    const T2x = cx + a_d * deltaXParallel - b_d * deltaXPerpendicular;
    const T2y = cy + a_d * deltaYParallel - b_d * deltaYPerpendicular;
    
    if(Math.round(getDistance(targetCenter, {x: T1x, y: T1y}) - targetRadius) !== 0) throw new Error("Tangent point does not lie on circumference");
    if(Math.round(getDistance(targetCenter, {x: T2x, y: T2y}) - targetRadius) !== 0) throw new Error("Tangent point does not lie on circumference");



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


const getCircleFromRect = ({x, y, width, height})=>{
    const center = { x: x + width / 2, y: y + height / 2 };
    const radius = getDistance(center, {x, y});
    if(Math.round(getDistance(center, {x, y}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    if(Math.round(getDistance(center, {x:x+width, y:y}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    if(Math.round(getDistance(center, {x:x+width, y:y+height}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    if(Math.round(getDistance(center, {x, y:y+height}) - radius) !== 0) throw new Error("Circle around rectangle fail to be equidistant from its corners");
    return {center, radius: Math.min(width / 2, height / 2)}
}


const getAngleFromCircles = (viewPoint, circles, maxAngle = Math.PI) => {
    const angle = circles.reduce((acc, circle) => acc + getViewingAngle(viewPoint, circle).angle, 0);
    if(angle >= maxAngle) throw new Error("Circles do not fit at current distance from viewpoint");
    return angle; 
}


const rotatePoint = (point, radiansAngle) => {
    const {distance, radians} = cartesian2Polar(point);
    return polar2Cartesian({distance, radians: radians + radiansAngle});
}


function expandMenuCircle(menuCenter, navRects, step = 100, maxAngle = Math.PI){
    try {
        return {
            angle: getAngleFromCircles(menuCenter, navRects.map(rect => getCircleFromRect(rect)), maxAngle),
            rects: navRects
        }
    }catch(e){
        return expandMenuCircle(menuCenter, navRects.map(rect => applyTranslatorToRect(rect, {deltaX: 0, deltaY: -1 * step})), step, maxAngle);
    }
}        










/* Main Function */
function positionMenuItem(){

    const angularSpace = Math.PI / 2;
    const angularAnchor = Math.PI;
    // const correctionCoefficientOnCircles = 1;//0.85; // Use 1 in doubt
    const menuExpansionSteps = 5; 

    const navs = Array.from(document.querySelectorAll(".nav__item"));
    const menu = document.querySelector(".hamburger-menu");

    const {center: viewPoint, radius: viewPointSize} = getCircleFromRect(menu.getBoundingClientRect())
    const {angle, rects} = expandMenuCircle(viewPoint, navs.map(nav => nav.getBoundingClientRect()), menuExpansionSteps, angularSpace);

    const angleGap = angularSpace/(navs.length - 1);
    const coordsArr = [{item: 'menu', radius: viewPointSize, ...viewPoint}];
    console.log("Total Anglular space from menu items: ", 180 * angle/Math.PI);
    console.log("Gap Between menu items: ", 180 * angleGap/Math.PI);

    
    rects.reduce((acc, rect, i)=> {
        const circle = getCircleFromRect(rect);
        // const {angle} = getViewingAngle(viewPoint, circle);
        const distance = getDistance(viewPoint, circle.center);
        // const coordsChange = polar2Cartesian({distance, radians: acc + (1 - correctionCoefficientOnCircles)*angle})
        const coordsChange = polar2Cartesian({distance, radians: acc})
        const coords = sumCoords(viewPoint, coordsChange);
        coordsArr.push({item: `nav${i}`, radius: circle.radius, ...coords })
        // moveNodeToCoords(navs[i], coords);
        putCoordsOnNode(navs[i], coordsChange);
        return acc + angleGap;
    }, angularAnchor);
    // }, angularAnchor + angleGap/2);


    console.log(coordsArr);
}


export default positionMenuItem;