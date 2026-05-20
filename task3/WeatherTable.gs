// обновляет погоду для всех городов в таблице
function updateWeather() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  // получаем все данные
  const data = sheet.getDataRange().getValues();
  // Начинаем со второй строки (0, (1)...)
  for (let i = 1; i < data.length; i++) {
    const city = data[i][0]; // Столбец A (Город)
    if (!city || typeof city !== "string" || city.trim() === "") continue;

    try {
      const weather = fetchWeather(city.trim());
      if (weather) {
        // Запись
        sheet.getRange(i + 1, 2).setValue(weather.temperature); // B - Температура
        sheet.getRange(i + 1, 3).setValue(weather.humidity); // C - Влажность
        sheet.getRange(i + 1, 4).setValue(weather.windSpeed); // D - Ветер
        sheet.getRange(i + 1, 5).setValue(new Date()); // E - Время
        sheet.getRange(i + 1, 6).setValue("OK"); // F - Статус
      } else {
        sheet.getRange(i + 1, 6).setValue("Упс... Город не найден");
      }
    } catch (error) {
      console.error(`Ошибка при обработке города ${city}:`, error);
      sheet.getRange(i + 1, 6).setValue("Ошибка");
    }
  }
}

// Вспомогательная функция - получает погоду по названию города
function fetchWeather(city) {
  // Получает координаты
  const geoUrl = `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(city)}&count=1&language=ru`;
  const geoResponse = UrlFetchApp.fetch(geoUrl, { muteHttpExceptions: true });

  if (geoResponse.getResponseCode() !== 200) throw new Error("Geo API error");

  const geoData = JSON.parse(geoResponse.getContentText());
  if (!geoData.results || geoData.results.length === 0) return null;

  const location = geoData.results[0];
  const lat = location.latitude;
  const lon = location.longitude;

  // Получает погоду
  const weatherUrl =
    `https://api.open-meteo.com/v1/forecast?` +
    `latitude=${lat}&longitude=${lon}&` +
    `current=temperature_2m,relative_humidity_2m,wind_speed_10m&timezone=auto`;

  const weatherResponse = UrlFetchApp.fetch(weatherUrl, {
    muteHttpExceptions: true,
  });

  if (weatherResponse.getResponseCode() !== 200)
    throw new Error("Weather API error");

  const weatherData = JSON.parse(weatherResponse.getContentText()).current;

  return {
    temperature: weatherData.temperature_2m,
    humidity: weatherData.relative_humidity_2m,
    windSpeed: weatherData.wind_speed_10m,
  };
}

// Создает меню в таблице при открытии
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu("Погода")
    .addItem("Обновить погоду для всех городов", "updateWeather")
    .addToUi();
}

// + таймер каждый час
function createHourlyTrigger() {
  ScriptApp.newTrigger("updateWeather").timeBased().everyHours(1).create();
}
