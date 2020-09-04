# Hello
## This is Jamie
This is My [Repo](https://github.com/JamieHoSzeYui/TESLA) to deploy your TESLA USERBOT 
NOW For using UserBot It is important to know Which Vars are used for What.
## envoirnment VARS

**API_KEY**: get this value from [here](https://telegram.dog/UseTGXBot).

**API_HASH**: you will get this value from where you get API_KEY .

**STRING_SESSION**: After getting above upper values you have to go to [session generator](https://session.uraniumcore.repl.run) it will ask to select option as t/p select t and sign in with phone number in international format as +918999993456.

**HEROKU_MEMEZ**: This Value Should be settled to "True" for deploying on heroku.

**HEROKU_API_KEY**: Get this value from [here](https://dashboard.heroku.com/account).

**HEROKU_APP_NAME**: This Value should be same as you filled app name on heroku.

**GITHUB_ACCESS_TOKEN**: Get this Value from [here](https://github.com/settings/tokens).

**GIT_REPO_NAME**: This value is require to do commits through Userbot.

**COUNTRY**: This value is required for Date , Time and Weather example:India.

**TZ_NUMBER**: If country is not set or giving error set this value example:+5.5 .

**TELEGRAPH_SHORT_NAME**: telegraph shortname for graph credits.

**OPEN_WEATHER_MAP_APPID**: Get your own APPID (API key) from [here](https://api.openweathermap.org/data/2.5/weather).

**GENIUS_API_TOKEN**: This value is required for using lyrics module get api token from [here](https://genius.com/developers).

**BOTLOG**: Incase you want to turn off logging, put this to false.

**BOTLOG_CHATID**: fill this with your private group id only work with supergroup only get id by giving command to haruka /id fill this value for skip starting error.

**PM_AUTO_BAN**: set this to True for PM protection.

**YOUTUBE_API_KEY**: This key required for YouTube search get this from [here](https://console.cloud.google.com).

**OCR_SPACE_API_KEY**: Required for image to text get OCR API Key for .ocr command. Get from [here](https://ocr.space/ocrapi).

**REM_BG_API_KEY**: API Key for .rbg command. Get from [here](https://www.remove.bg/api).

**ANTI_SPAMBOT**: Kicks spambots from groups after they join ,Requires admin powers in groups to kick.

**ANTI_SPAMBOT_SHOUT**: Report spambots to @admins in groups after they join, just in case when you don't have admin powers to kick that shit yourself.

**TMP_DOWNLOAD_DIRECTORY**: don't change this value for better assistance.

**USER_TERM_ALIAS**: Terminal alias name.

**QUOTES_API_TOKEN**: same as quotly but require api token. Get token from [here](http://antiddos.systems).

**CLEAN_WELCOME**: When a new person joins, the old welcome message is deleted.

**G_DRIVE_CLIENT_ID**: for gdrive values refer to gdrive section below.

**LASTFM_API**: API Key for Last.FM module. Get one from [here](https://www.last.fm/api/account/create).

**LASTFM_SECRET**: SECRET Key for Last.FM module. You will get this value from upper link.

**LASTFM_USERNAME**: Last.FM Username.

**LASTFM_PASSWORD**: Last.FM Password.

**BIO_PREFIX**: Prefix for Last.FM Module Bio.

**DEFAULT_BIO**: Default profile bio.

**ALIVE_NAME**: Name for .alive command.

**G_DRIVE_CLIENT_SECRET**: Refer to Gdrive section below.

**G_DRIVE_AUTH_TOKEN_DATA**: Refer to Gdrive section below.

**LYDIA_API_KEY**: This Module Needs CoffeeHouse API to work. so Join [here](https://telegram.dog/IntellivoidDevhere) and send #activateapi and follow instructions.

**WEATHER_DEFCITY**: City name for weather module.

**LOGSPAMMER**: Set this to True in case you want the error logs to be stored in the userbot log group, instead of spitting out the file in the current chat, requires a valid BOTLOG_CHATID to be set.

# HEROKU
What is Heroku?
Answer:-Heroku is a cloud platform as a service (PaaS) supporting several programming languages. One of the first cloud platforms, Heroku has been in development since June 2007, when it supported only the Ruby programming language, but now supports Java, Node.js, Scala, Clojure, Python, PHP, and Go.[1][2] For this reason, Heroku is said to be a polyglot platform as it has features for a developer to build, run and scale applications in a similar manner across most languages. Heroku was acquired by Salesforce.com in 2010 for $212 million.
## Want to deploy on HEROKU

Want to make account click [here](https://signup.heroku.com).

if you already have or created one now click [here](https://heroku.com/deploy?template=https://github.com/ElytrA8/TESLA/tree/TESLA) for deploying.

Now fill the required values

And Done your userbot should be alive now

## Gdrive
[Click here](https://da.gd/so63O)

Login to your gmail.com account. It is recommended to use a gmail.com for creating the API.

Select Create a Project, Accept the Terms of Service, and select your Country of Residence.

Click on Agree and Continue button.

Click on Get Credentials button.

In the new screen, scroll down.

For Which API are you using? select Google Drive API from the dropdown.

For Where will you be calling the API from? select Other UI (e.g. Windows, CLI tool)

For What data will you be accessing? select User data.

Click on What credentials do I need?

A pop-up will appear.

Click on SET UP CONSENT SCREEN.

A new tab will open.

Give your application name, and logo that should display on the consent screen.

Since this is going to be used for your personal purposes, we do not need verification. 

Google allows the first 100 users to be authenticated without the verification status.

Scroll Down and Click on the Save button.

You can now close this tab, and return to the previous tab.

Click on the Refresh button.

Click on the Create OAuth Client ID button.

Click on the Done button.

The page will get refreshed. 

Click on the Edit button.

Copy the Client ID and Client secret.

Add the Client ID to the G_DRIVE_CLIENT_ID key, in Heroku Environment Variable.

Add the Client secret to the G_DRIVE_CLIENT_SECRET key, in Heroku Environment Variable.

This plugin also requires the BOTLOG_CHATID to be set.

Send a small file, in your BOTLOG_CHATID Group.

[This process should be done after deploying]

Reply .gd to this file.

A link will appear. 

**The below six steps should be done in less than 1 minute.**

Open the link in your browser, and login to the Google Drive account.

All gDrive functionalities will be done on this account.

This need same account that you created your API in.

After login, it will display a code. 

Reply this code to the in your BOTLOG_CHATID to the message from which you opened link.

It will now give a txt file 

Open and copy code

And set it in G_DRIVE_AUTH_TOKEN_DATA IN HEROKU VAR

Gdrive is now ready to use.

## Youtube
Go [here](https://console.developers.google.com/apis/dashboard)

Open menu

Select same project as gdrive

Reopen menu

In api & services

Select libraries

Search YouTube data

Select YouTube data api

Click on enable api

Open menu and now goto api & services

Select credentials

Now from right side there is three dot button and down from it there is one more same button

Click on button and Create Credentials

Then choose (help me choose)

Same as gdrive but select YouTube data api

Where will you be calling the API from? --> select other ui eg. Windows

What data will you be accessing? --> select public data 

Click on What credentials do I need

It will give a api key now

If not goto menu api&services --> credentials 

And in API Keys section 

There should be one api key 

Open it and copy 

Now add it to heroku vars with YOUTUBE_API_KEY

## TRANSFER
Can be Used with terminal command 
For Example :-
```
.term ./transfer <config> <file location>
Like 
.term ./transfer bit ./downloads/sticker.webp
```
Configs can be found in table 


|  Name   | Site  | Limit | Provider |
|  ----  | ----  |  ----  |  ----  |
| Airportal | https://aitportal.cn/ | - | Aliyun |
| bitSend | https://bitsend.jp/ | - | OVH |
| CatBox | https://catbox.moe/ | 100MB | Psychz |
| CowTransfer | https://www.cowtransfer.com/ | 2GB | Qiniu |
| GoFile | https://gofile.io/ | - | - |
| TmpLink | https://tmp.link/ | - | - |
| Vim-cn | https://img.vim-cn.com/ | 100MB | CloudFlare |
| WenShuShu | https://www.wenshushu.cn/ | 5GB | QCloud |
| WeTransfer | https://wetransfer.com/ | 2GB | CloudFront |
| FileLink | https://filelink.io/ | - | GCE |
| Transfer.sh | https://transfer.sh/ | - | Hetzner |
| Lanzous | https://www.lanzous.com/ | login only | - |

Config values

| config | site name | website |
|  ----  | ----  |  ----  |
|  arp  |  Airportal  |  https://aitportal.cn/ |
|  bit  |  bitSend  |  https://bitsend.jp/ |
|  cat  |  CatBox  |  https://catbox.moe/
|  cow  |  CowTransfer  |  https://www.cowtransfer.com/ |
|  gof  |  GoFile  |  https://gofile.io/ |
|  tmp  |  TmpLink  |  https://tmp.link/ |
|  vim  |  Vim-cn  |  https://img.vim-cn.com/ |
|  wss  |  WenShuShu  |  https://www.wenshushu.cn/ |
|  wet  |  WeTransfer  |  https://wetransfer.com/ |
|  flk  |  FileLink  |  https://filelink.io/ |
|  trs  |  Transfer.sh  |  https://transfer.sh/ |
|  lzs  |  Lanzous  |  https://www.lanzous.com/ |




## Extras

Want to contact Owner/lead dev click [here](https://telegram.dog/ElytrA8)

Want to join support group click [here](https://telegram.dog/PROJECT_TESLA)

ot group join [here](https://telegram.dog/ElytrA8CT)

