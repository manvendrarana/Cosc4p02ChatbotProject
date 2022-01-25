const webdriver = require("selenium-webdriver");
const until = webdriver.until;
const By = webdriver.By;
goldNum = 0;

const driver = new webdriver.Builder().forBrowser("chrome").build();

let parseURL = async(url) =>
{
    await driver.get(url);
    let element = await driver.findElement(By.className('ResultEventContainer'));
    await driver.wait(until.elementIsVisible(element), 15000)
    .then(() =>
    {
        const array = driver.findElements(By.className('ResultEventContainer'));
        array.then((ele) =>
        {
            ele.forEach((arrayItem) =>
            {
                const nextElement = arrayItem.findElement(By.className('ResultEventHeaderContainer'));
                nextElement.then((item) =>
                {
                    var goldNum = 0;
                    item.getText().then((result) =>
                    {
                            console.log(result)
                            goldNum = goldNum + 1;

                    });
                });
            });
        });
    });
}

parseURL("https://cg2015.gems.pro/Result/ShowPerson.aspx?Person_GUID=7F1079FC-AF27-4858-82AB-9ECCBD675D7E&SetLanguage=en-CA")

/* results:
Short Track - 500 m Female
: 203
Final position: Gold
Short Track - 1000 m Female
: 203
Final position: Silver
Short Track - 1500 m Female
: 203
Final position: Gold
Short Track - 3000 m Relay Female
Team: QC
: 203
Final position: Gold
Short Track - 3000m Points Race Female
: 203
Final position: Bronze
*/
