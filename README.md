# Valentine
![alt text](https://i.imgur.com/OLJURRD.png)
A Tinder Client on Discord?! What is this madness?!

Warning: This bot is in a very early stage and can and will probably break! Please help me by [reporting](https://github.com/antoniomsantos99/Valentine/issues) it's issues.

This bot will not gather any information about you, it's just the middleman between tinder and discord.

# Config

Since i should't comment on json files i'll explain them here:

"BOT_TOKEN": Here you'll put your discord bot's token ([GET ONE HERE](https://discordapp.com/developers/applications/me))

"FB_TOKEN" : For the bot to access your tinder account it'll need your Facebook token ([HOW TO GET](https://gist.github.com/taseppa/66fc7239c66ef285ecb28b400b556938)) (thanks taseppa!)

"WHITELIST" : Leave this blank if you want anyone to have permission to use the bot or whitelist it by putting your id here (Ex:"JohnDoe#0000")

## How to install
Run Install.bat OR

Since Pynder is somewhat outdated i am using a pull request from it which is more up to date use these commands to install it:
````bash
git clone https://github.com/charliewolf/pynder.git
cd pynder
git fetch origin +refs/pull/211/merge
git checkout -qf FETCH_HEAD
python -m pip install --force-reinstall --no-deps .
````
Then install the rest using:
````bash
pip install -r requirements.txt
````
And it should be all done!

## License
[GPL](https://choosealicense.com/licenses/gpl-3.0/)
