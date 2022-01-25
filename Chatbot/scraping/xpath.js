// requirements
const webdriver = require("selenium-webdriver");
chrome    = require('selenium-webdriver/chrome')
options = new chrome.Options();
options.addArguments('headless');
const until = webdriver.until;
const By = webdriver.By;
var map = webdriver.promise.map;

// variables
goldNum = 0;
silverNum = 0;
bronzeNum = 0;
let stringArray = [];

// building selerium browser
const driver = new webdriver.Builder().forBrowser("chrome").setChromeOptions(options).build();

// parse url method, calls medalCalculator, a helper method
// for calculating the medals and printing to console
let parseURL = async(url) =>
{
    await driver.get(url);
    let element = await driver.findElement(By.className('ResultEventContainer'));

    await driver.wait(until.elementIsVisible(element), 15000)
        .then((res) =>
        {
            var elems = driver.findElements(By.xpath('//div[@class="ResultEventContainer"]/div[@class="ResultEventHeaderContainer"]'))
            map(elems, e => e.getText())
        .then((values) =>
            {
                console.log(values);
                stringArray = values;
                medalCalculator();
            });

        });
}

// call method for parsing the URL
parseURL("https://cg2015.gems.pro/Result/ShowPerson.aspx?Person_GUID=7F1079FC-AF27-4858-82AB-9ECCBD675D7E&SetLanguage=en-CA");

// method for calculating bronze/silver/gold medals and printing to console info
let medalCalculator = () =>
{
    console.log("Printing array\n")
    stringArray.forEach(x => {
        console.log(x)
        if(x.includes("gold") || x.includes("Gold"))
            {
                goldNum++;
            }
        if(x.includes("bronze") || x.includes("Bronze"))
            {
                bronzeNum++;
            }
        if(x.includes("silver") || x.includes("Silver"))
            {
                silverNum++;
            }
    });
    console.log("\nGold medals won: " + goldNum);
    console.log("\nSilver medals won: " + silverNum);
    console.log("\nBronze medals won: " + bronzeNum);

    driver.close();
    console.log("\n driver closed");
}

/* '//div[@class="ResultEventContainer"]/div[@class="ResultEventHeaderContainer"]/p[3]' would access 3rd <p>


Output:

Printing array

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

Gold medals won: 3

Silver medals won: 1

Bronze medals won: 1

 driver closed
*/
