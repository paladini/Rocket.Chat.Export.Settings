# Rocket.Chat Settings Exporter

Export your settings from a Rocket.Chat instance and import it into another Rocket.Chat instance.

## How to use?

```
git clone https://github.com/paladini/Rocket.Chat.Export.Settings.git
cd Rocket.Chat.Export.Settings
python settings_exporter.py [configs to export] <origin_mongodb_ip> <destiny_mongodb_ip>
```

Example:
```
# In this example we will export SMTP (-s) and File Upload (-u) configs.
python settings_exporter.py -su 172.12.0.2:27017 172.12.0.5:27017
```