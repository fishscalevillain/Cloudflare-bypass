# Cloudflare-bypass

Решил порофлу закинуть мб кому то поможет, если у вас не будет воркать мне похуй. Репозиторий решает проблему того что undetected_chromedriver обходит cloudflare но приходиться тыкать в чекбокс, а чекбокс в shadowroot поэтому вот вам код который тыкает по нему через поиск координат чекбоскса.

**Зависимости**
```
pip install selenium
pip install undetected_chromedriver
pip install --upgrade setuptools # В undetected_chromedriver устаревший distutils поэтому надо обновить
