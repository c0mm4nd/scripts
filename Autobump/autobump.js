// ==UserScript==
// @name         AutoBump
// @namespace    https://c0mm4nd.com/
// @version      0.1.1
// @description  autobump the thread in bitcointalk
// @author       Command M
// @match        https://bitcointalk.org/*
// @grant        none
// ==/UserScript==


(async function () {
    'use strict';
    function getElementByXpath(path) {
        return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    }

    console.log('autobump loaded', new Date())

    let ele = getElementByXpath("//*[@id=\"bodyarea\"]/table[1]/tbody/tr/td[2]/table/tbody/tr/td[2]/a[6]")
    if (ele != null) {
        let url = ele.href
        let res = await fetch(url)
        if (res.status !== 200) {
            console.log('failed to autobump: ', url, res)
        } else {
            console.log('autobumped')
        }
    }

    setTimeout(() => { location.reload() }, 1000 * 60 * 10) // fresh page every 10min
})();