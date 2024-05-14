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

Then, we need to create a python environment & install the dependencies.

- Open a terminal and go to this folder:

```
$ cd <YourPath>/Bot-MyBrute
```

- On MacOS, create a python environment:

```
$ python3 -m venv myVenv
```

- Enter the python environment:

```
$ source myVenv/bin/activate
```

- Install the dependencies:

```
$ pip3 install python-dotenv selenium
```

- Now create a copy of the environment file:

```
$ cp .env.example .env
```

- Open the new `.env` file created and replace the templates by your `PASSWORD`, `BASIC_ACCOUNTS` & `BEST_ACCOUNTS` as shown in the file.

## Run Bot

All is set-up! You can now run the bot each time you want to automate your gameplay:

- Make sure the MyBrute game language is set to French.

- Open terminal and go to this folder:

```
$ cd <YourPath>/Bot-MyBrute
```

- Make sure you are in the python environment *(with `(myVenv)` on the left)* or run it:

```
$ source myVenv/bin/activate
```

- Run the bot:

```
$ python3 mybrute.py
```

When a brute needs to level up, you will receive the notification `{BruteName} - NEEDS TO LEVEL UP`, and the bot will go to the next Brute. Same if your brute wins a tournament, you will get this notification `{BruteName} - WINS A TOURNAMENT! HE CAN RANK UP!`.

- You can then level up your brutes by runing this script:

```
$ python3 level-up.py
```

