# Rocket.Chat Settings Exporter

Export your settings from a Rocket.Chat instance and import it into another Rocket.Chat instance.

## How to use?

```
git clone https://github.com/paladini/Rocket.Chat.Export.Settings.git
cd Rocket.Chat.Export.Settings
python settings_exporter.py [configs to export] <origin_mongodb_ip> <destiny_mongodb_ip>
```

Want more? Try `python settings_exporter.py --help`.

### Example

In the following example we will export SMTP (-s) and File Upload (-u) configs from a Rocket.Chat instance that has it's MongoDB database running at 172.12.0.2 (port 27017) to another Rocket.Chat instance that has it's database running at 172.12.0.5 (port 27017).

```
python settings_exporter.py -su 172.12.0.2:27017 172.12.0.5:27017
```

## How to contribute?

Contributions are very welcome! Feel free to [suggest new features here](https://github.com/paladini/Rocket.Chat.Export.Settings/issues) or even fork this project and implement your features by yourself :) 