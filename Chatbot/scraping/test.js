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
