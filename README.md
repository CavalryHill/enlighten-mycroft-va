# enlighten-voice-assistant

## System Using at The Moment
 + Raspberry Pi 4
 + 32 GB SD-Card


## Flash Picroft Image to Raspberry Pi
First, go get yourself [Picroft](https://github.com/MycroftAI/enclosure-picroft), please make sure you download the `stable image` on `2020-09-07`.

then follow up the [RPi Official Document](https://github.com/MycroftAI/enclosure-picroft) to flash it into Raspberry Pi. 

> [!CAUTION]
> Please making sure you're using Wi-Fi 2.4G for Picroft to create connection. I was using 5.0G and finally found out the problem during Mycroft-Setup-Wizard, so I'm not sure if setting up Wi-Fi insde Imager would work or not. But if you succeed to connect the device with SSH, congrats you save cost for a useless, expensive HDMI converter.  

## Setup Picroft
> [!CAUTION]
> I recommend setting up everything during the Mycroft-Setup-Wizard to avoid manual file edits. The `mycroft-setup-wizard` command has been broken for a long time actually.

> [!TIP]
> Embrace the guided setup for clearer instructions, or why would you turn down such hospitality?

![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/1048bb9a-33a4-463e-b048-9ae43067513d)

### Reading the Logs
For debugging purpose, we oftenly need to check the logs for exceptions, and you could find them at `/var/log/mycroft`  
![Screenshot 2023-12-16 110332](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/c4464a29-6750-4739-86d5-0c1a4c948851)

> [!NOTE]  
> You may pay a visit to [Official Document](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/troubleshooting/log-files) to get better known with these files  

### Updateing Packages
Guessing the official forgot to defined version of python package, much of them are not working with outdated `pip` and `package`, please do as following. 
`mycroft-pip install --upgrade pip`

### Paring Device
1. Register or Login your account at [Mycroft AI](https://home.mycroft.ai/). 
2. On the left side-menu >> My Mycroft >> Devices. 
3. Setup the default config for all device on the first time.
4. Press 'Add Device' and connect your Picroft with the 6-digit-code provided in Mycroft CLI >> History.

You should see something alike as below, and please make sure the `mycroft-version` is displayed to confirm the connection. 
![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/a0b9e2ce-69af-42db-aeff-4432821f1e6e)

### Changing Text-to-Speech Engine
If you can hear the audio output while mic testing, but no sound while running response in CLI, likewise, it's probally the default package of `mycroft-mimic3-tts` is also outdated and causing no sound output. I've met the error but enable to fix the python package conflict. So, I simply change the TTS module to Google. 
Simply run `mycroft-config set tts.module "google"`, then the user config will change automatically. 

If you wish to change the language output, may please hit `mycroft-config edit user`, you should see the file as below. 
```
{
  "max_allowed_core_version": 21.2,
  "tts": {
    "module": "google",
  }
}
```
then change it like so (example for English(UK))
```
{
  "max_allowed_core_version": 21.2,
  "tts": {
    "module": "google",
    "google": {
      "lang": "en-uk"
    }
  }
}
```

> [!NOTE]
> You may visit [Officual Document](https://mycroft-ai.gitbook.io/docs/using-mycroft-ai/customizations/tts-engine) for more choices on TTS Engine, or you may vist [gTTS](https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang) to see the supported language and accent.

## Client Bus
Although simply using the Mycroft provide much function, we want to catch or set the I/O to make more expansion. 

### Basic Usage
After the fixes above, you should be able to use the CLI and getting audio output now. You can simply input some text in CLI, or try-out the wake word, after hearing a alert sound, it start recording. 

### Custom Skill for Music
![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/ccaf3d6d-f183-4e55-9f0a-64dcaf916dc4)

There are finely built Mycroft-Skills in Marketplace for Spofity and Pandora already, but as a Hi-Res Audio Purchaser, I don't wish to waste more money on stream service subscription cost, so I just tried hard to fetch music on YouTube by searching for URL, and you may check [python-file] to see how I archieve this. 

## Nextcloud Server
With much storage un-used, I hit upon this idea to use it as NextCloud Server to store 'secret files' and also work as where Mycroft downloads the audio to. 

Folllow up the guide [here](https://raspberrytips.com/install-nextcloud-raspberry-pi/) (2nd method) to host nextCloud without flashing the image. 

### Updating Linux Settings
![Screenshot 2023-12-30 143613](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/0201e185-08a3-4c01-a9bb-c344e0d9876e)
The default settings of Mycroft Stable Image actually stopped you from any changes to Operating System (OS), so you need to use the following command to rewrite the settings and also update OS.  
`sudo apt-get --allow-releaseinfo-change update`  

### Installing Required Package
![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/45849a83-7250-46c3-b700-5296c3e502bb)  
Here's the [doc](https://docs.nextcloud.com/server/latest/admin_manual/installation/system_requirements.html) of system requirements. I decided to use php8.2.  

Yet on Raspberry Pi, the latest PHP version recognized by apt is merely version 7.3, so we need to make following changes to install higher versions: 
1. Run the following commands to create source of PHP  ```sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
echo "deb https://packages.sury.org/php/ buster main" | sudo tee /etc/apt/sources.list.d/php.list
sudo apt update```
2. Run `sudo apt install php8.2` to install core functions of PHP 8.2.
3. Run `sudo apt install php8.2-zip php8.2-xml php8.2-mbstring php8.2-gd php8.2-curl` to install all required extensions.
4. Run `sudo apt install php8.2-mysql` to ensure database drivers.

> [!CAUTION]
> Keep away from PHP Official Site to download tar.gz for version 8.2 to your local personal computer, my anti-virus software `Kaspersky` reported it with `Torjan`. Better safe than sorry. 

> [!TIP] You can check the version of PHP by running `php -v`.
![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/76b7e7bd-10fb-4ac7-8f7a-e266c1393a9d)  

After the installation of PHP, we need to connect it with our web server. 

Then to host a web server, I am using my most accustomed launcher -- Apache2, which the config file is also similar to Nginx. Now we followed the instructions to install our needs. Let's install MariaDB along side, which should be version 10.3.  
1. Run `sudo apt install apache2 mariadb-server libapache2-mod-php` to install required package.  
2. If you have any older version, run `sudo a2dismod php<old-version>` to disable it first.  
3. Run `sudo a2enmod php8.2` to enable the module, then restart your Apache server.  

### Setting-Up Database
Ere we jump into nextcloud console, we need to configure a database for it's data beforehand. 
1. Run `sudo mysql` to get into MySQL with root without password.
2. Run `CREATE USER 'nextcloud' IDENTIFIED BY '<PASSWORD>';` to create a new MySQL user.
3. Run `CREATE DATABASE nextcloud;` to create a new database, then run `GRANT ALL PRIVILEGES ON nextcloud.* TO 'nextcloud'@localhost IDENTIFIED BY '<PASSWORD>';` to give user the permission of the newly created database.
4. Run `FLUSH PRIVILEGES;` to reload settings, then run `quit;` to leave MySQL console. 

### Installing Nextcloud Web-Pack
Thanks to manys' efforts, there's also public released Nextcloud web-pack, please followed the instructions below. 
1. Use `cd /var/www` to get under the default Apache web-pack storage.
2. Use `sudo wget https://download.nextcloud.com/server/releases/latest.zip` to start downloading the `ZIP` file.
3. Use `sudo unzip latest.zip` to un-zip the web-package, which should be named `nextcloud`. 
![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/89d32b70-aac7-4465-8b32-47334a721f66)

### Implemeting Nextcloud Web-Pack
To have the easiest way, we can simply change the folder name `nextcloud` to `html`, the target of default Apache config. Although I always recommend to create a new config file, let's have-an-eye on it for the basic to everyone. 

1. After re-naming, use `sudo service apache2 restart` to restart the service and  
2. Use `sudo chown www-data:www-data html -R` in directory `/var/www` to give the Apache permission to read the folder, or there will be a blank webpage.  
3. the new website should be host on <DEVICE_IP>:80.  ![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/d13c259b-9474-4ba0-aca1-b9eb98dfe72f)
4. Follow the steps then install nextcloud.
5. Get youself a nice drink and dessert to watch a movie, just don't close the long-awaiting installation.
6. After installation for file storage is done, it will ask you if other functions is needed, let's just skip them.  ![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/4c64c971-86bb-4ffa-8910-02481425b809)
7. Hurrah, we've settled our own cloud storage in the Raspberry Pi now.  ![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/df6b0aef-3087-4072-8a40-56c226c24007)

## Device Buildup
It's finally time for us to build our device with electronic devices. Due to time and difficulity, I only got following done. 
### Time Display
> [!NOTE]  
> The source code is named `time_display.py` inside folder `python-ext`

I'm using the component based on TM1637, which have python package `tm1637` for easy way to display numbers. Let's move on.  
1. Run `mycroft-pip install raspberrypi-tm1637` to get the package first.  
2. For the circuit, connect `CLK` with `GPIO23`, and `DIO` with GPIO24. Find any ground pin for `GND` and 5V for the `VCC`.
3. Run `python time_display.py` to manually test it, then you can add it into `auto_run.sh` with its path.
> [!TIP]
> You can change brightness higher from 0 to 7, at [Line 13]

![20240107_131353](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/44cbafcf-9ef4-4f4f-b04a-1d9ec4e5f071)


## Reference
> Mycroft  
>  - [Mycroft Offical Doc](https://mycroft-ai.gitbook.io/docs/)

> LED Skill for Mycroft  
> - [Example Code](https://github.com/arother/picroft-led)  

> gTTS  
>  - [gTTS Offical GitHub](https://github.com/pndurette/gTTS/blob/main/gtts/tts.py#L18)  
>  - [Detailed Doc](https://gtts.readthedocs.io/en/latest/module.html)  

> Download from YouTube  
>  - [Python Library - PyTube](https://pytube.io/en/latest/)  
>  - [Changing File Extensiom from .mp4 to .mp3](https://stackoverflow.com/questions/47420304/download-video-in-mp3-format-using-pytube)

> FLASK Website
>  - [Offical Doc of FLASK SocketIO](https://flask-socketio.readthedocs.io/en/latest/)

> Nextcloud  
>  - [Offical Site](https://nextcloud.com/)  
>  - [Install Tutorial for Apache Hosting](https://raspberrytips.com/install-nextcloud-raspberry-pi/)  
>  - [Get Higher PHP Version - 1](https://janw.me/raspberry-pi/installing-php82-rapsberry-pi/)  
>  - [Get Higher PHP Version - 2](https://lindevs.com/install-php-on-raspberry-pi)  

> TM1637  
>  - [TM1637 Tutorial](https://github.com/depklyon/raspberrypi-tm1637)

## If Interested  
> Spotify  
>  - [Python Library - Spotipy](https://spotipy.readthedocs.io/en/2.22.1/)  
>  - [Spotify Developer API](https://developer.spotify.com/)  
