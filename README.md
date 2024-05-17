Федерации спортивного туризма России pereval.online (далее - ФСТР) заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Турист с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:

Информацию о себе:
Фамилия;
Имя;
Отчество;
Электронная почта;
Номер телефона.
Название объекта;
Координаты объекта и его высоту;
Уровень сложности в зависимости от времени года;
Несколько фотографий.
После этого турист нажимает кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод Pereval.

Метод:

POST/perevals/
принимает JSON в теле запроса с информацией о перевале. Пример JSON-а:

{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", //что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "tourist_id": {"email": "qwerty@mail.ru", 		
        "last_name": "Пупкин",
		 "first_name": "Василий",
		 "patronymic": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coord_id":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
Результат метода: JSON

status — код HTTP, целое число:

500 — ошибка при выполнении операции;

400 — Bad Request (при нехватке полей);

200 — успех.

message — строка:

Причина ошибки (если она была);

Отправлено успешно;

Если отправка успешна, дополнительно возвращается id вставленной записи.

id — идентификатор, который был присвоен объекту при добавлении в базу данных.

Примеры oтветов:

{ "status": 500, "message": "Ошибка подключения к базе данных","id": null}

{ "status": 200, "message": null, "id": 42 }

После того, как турист добавит в базу данных информацию о новом перевале, сотрудники ФСТР проведут модерацию для каждого нового объекта и поменяют поле status.

Допустимые значения поля status:

'new';
'pending' — модератор взял в работу;
'accepted' — модерация прошла успешно;
'rejected' — модерация прошла, информация не принята.
