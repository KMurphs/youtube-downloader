// Get all youtube videos links for a channel e.g. https://www.youtube.com/c/<SomeChannel>/videos
Array.from(document.querySelectorAll(".yt-simple-endpoint.style-scope.ytd-grid-video-renderer")).map(el => el.href)


r = new RegExp("^[0-9]( hour)")
Array.from(document.querySelectorAll("a.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail")).filter(el => el.querySelector("span") && r.test(el.querySelector("span").ariaLabel)).map(el => el.href)
Array.from(document.querySelectorAll("a.yt-simple-endpoint.inline-block.style-scope.ytd-thumbnail")).filter(el => el.querySelector("span") && el.querySelector("span").innerText.split(":").length === 3).map(el => el.href)


Array.from(document.querySelectorAll("#contents.style-scope.ytd-playlist-video-list-renderer #content.style-scope.ytd-playlist-video-renderer > a")).map(el => el.href)
