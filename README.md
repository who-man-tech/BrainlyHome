# BrainlyHome

База умного дома основанная на Raspberry Pi и микроконтроллерах.

## Логика работы:
Вся логика умного завязана на комнатах дома,
в которых имеются модули(сенсоры, управлемые устройсва).
Но не смотрая на это можно подключать сенсор одной комнаты
к управляемому устройству другой комнаты. 
Например: Если входная дверь открылась, то включаем чайник на кухне.
Мы подключаем датчик двери в прихожей к чайнику в кухне

## Как это работает:
Для общения между микроконтроллерами используется mqtt протокол.
При включении Raspberry ищет все модули, к которым можно подключится.
Затем проверяет их id, если такой модуль уже был добавлен 
раннее(имеется в файле сохранений), то устанавливаем ему тип, комнату,
статус, друзей(id модулей, которым он подключен)