# Bot MyBrute

This bot has to objective to automate the gameplay of [MyBrute](https://brute.eternaltwin.org/).

With this bot, you can xp your game character without any actions.

![](./img/MyBrute.png)

## Pre-requisite

- `Python3` already installed.
- `pip` already installed.
- `Google Chrome` already installed.

Clone the repository:

```
$ git clone https://github.com/Sparadrap1101/Bot-MyBrute
```

## Set-up

First, you need to install your chrome driver.

- Verify you Chrome version:

  - Open `Google Chrome`.

  - Go to `Three dot icon > Help > About Google Chrome`.

  - Look at your Chrome version (for example `Version 120.0.6099.129`).

- Install your chrome driver in this folder:

  - For 120+ versions, go to [this link](https://googlechromelabs.github.io/chrome-for-testing/), select your version & platform, and follow the url of the `chromedriver` binary.

  - Download will start, unzip it and add the `chromedriver` file to this `Bot-MyBrute` folder.

Then, we need to install the `selenium` library.

- Open a terminal and go to this folder:

```
$ cd <YourPath>/Bot-MyBrute
```

- Install `selenium` on Windows:

```
$ pip install selenium
```

- Install `selenium` on MacOS:

```
$ pip3 install selenium
```

- Now create a copy of the environment file:

```
$ cp .env.example .env
```

- Open the new `.env` file created and replace the templates by your `password` & `bruteNames` as shown in the file.

## Run Bot

All is set-up! You can now run the bot each time you want to automate your gameplay:

- Make sure the MyBrute game language is set to French.

- Open terminal and go to this folder:

```
$ cd <YourPath>/Bot-MyBrute
```

- Run the bot:

```
$ python3 mybrute.py
```

When a brute needs to level up, you will receive the notification `{BruteName} NEEDS TO LEVEL UP`, and the bot will go to the next Brute. You can then level up the brute yourself and restart the bot starting with the account index you want in order to finish the remaining fights.
