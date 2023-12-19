# enlighten-voice-assistant

## Picroft 燒錄
First, go get [Picroft](https://github.com/MycroftAI/enclosure-picroft), please make sure you download the `stable image` on `2023-09-07`.

then follow up the [RPi Official Document](https://github.com/MycroftAI/enclosure-picroft) to install

> [!CAUTION]
> Please making sure you're using Wi-Fi 2.4G for Picroft to create connection. I was using 5.0G and finally found out the problem during Mycroft-Setup-Wizard, so I'm not sure if setting up Wi-Fi insde Imager would work or not. But if you succeed to connect the device with SSH, congrats you save cost for a useless, expensive HDMI converter.  

## Picroft 架設
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

### 套件升級
Guessing the official forgot to defined version of python package, much of them are not working with outdated `pip` and `package`, please do as following. 
`mycroft-pip install --upgrade pip`

### Paring Device
1. Register or Login your account at [Mycroft AI](https://home.mycroft.ai/). 
2. On the left side-menu >> My Mycroft >> Devices. 
3. Setup the default config for all device on the first time.
4. Press 'Add Device' and connect your Picroft with the 6-digit-code provided in CLI >> History. 

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
