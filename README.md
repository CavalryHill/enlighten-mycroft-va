![Screenshot 2023-12-16 111349](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/d1556508-7c33-4678-8dcf-0dedc4b312da)# enlighten-voice-assistant

## Picroft 燒錄
```
請確保所使用的 Wi-fi 為 2.4G
```

## Picroft 架設
首次開機會啟動 mycroft-wizard，請確保麥克風與音響在此階段完成設置，因為預設的指令已失效

![image](https://github.com/CavalryHill/enlighten-mycroft-va/assets/92420621/1048bb9a-33a4-463e-b048-9ae43067513d)

### 套件升級
可能是官方當初設計時沒有設定 pip 下載指定套件版本，導致更新的套件無法在舊的 pip 環境執行  
`mycroft-pip install --upgrade pip`


### 更換 TTS 模型
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
