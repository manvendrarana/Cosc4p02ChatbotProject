const webdriver = require("selenium-webdriver");
chrome    = require('selenium-webdriver/chrome')
options = new chrome.Options();
options.addArguments('headless');
const until = webdriver.until;
const By = webdriver.By;

goldNum = 0;

const driver = new webdriver.Builder().forBrowser("chrome").setChromeOptions(options).build();

let parseURL = async(url) =>
{
    await driver.get(url);
    let element = await driver.findElement(By.className('ResultEventContainer'));

    await
        driver.wait(until.elementIsVisible(element), 15000).then(() => {
        driver.findElements(By.xpath('//div[@class="ResultEventContainer"]/div[@class="ResultEventHeaderContainer"]')).then((elements) => {
                    for(var i = 0; i < elements.length; i++)
                    {
                        elements[i].getText().then(function(text) {
                            if(text.includes("gold") || text.includes("Gold"))
                            {
                                console.log(text)
                                goldNum = goldNum + 1;
                            }
                        })

                    };
                });
            });
}

parseURL("https://cg2015.gems.pro/Result/ShowPerson.aspx?Person_GUID=7F1079FC-AF27-4858-82AB-9ECCBD675D7E&SetLanguage=en-CA")
// '//div[@class="ResultEventContainer"]/div[@class="ResultEventHeaderContainer"]/p[3]' would access 3rd <p>
