## 创建models结构顺序

### 第一步
 - 在settings中配置数据库
   ```Shell
      DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'userdb',
           'USER': 'postgres',
           'PASSWORD': '123456',
           'HOST': '192.168.179.151',
           'PORT': '5432',
       },
       'school': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'userdb',
           'USER': 'postgres',
           'PASSWORD': '123456',
           'HOST': '192.168.179.151',
           'PORT': '5432',
           'OPTIONS': {
               'options': '-c search_path=school'
           },
       }
   }
   ```
 - 在根目录创建settings文件夹，在文件夹下创建route.py文件
 - 在项目的settings.py文件中增加数据库与APP的映射配置，支持每个APP都使用不同的数据库
   ```Shell
   
   ```
   ```Shell
   # 引入数据库路由配置
   DATABASE_ROUTERS = ['settings.router.DatabaseAppsRouter']
   # 数据库与APP的映射配置
   DATABASE_APPS_MAPPING = {
       'sqlcmd': 'default',
       'school': 'school',
   }
   ```

### 第二步

 - 使用python3 manage.py startapp school创建app
 - 在setting.py文件中注册创建的app，如school
 - 使用python3 manage.py makemigrations school生成迁移文件
 - 使用python3 manage.py migrate迁移生成二维表(python3 manage.py sqlmigrate school 0001 --database=school)
 - 创建超级管理员账号。

   ```Shell
   (venv)$ python manage.py createsuperuser
   Username (leave blank to use 'hao'): jackfrued
   Email address: jackfrued@126.com
   Password: 
   Password (again): 
   Superuser created successfully.
   ```
   
 - 启动Web服务器，登录后台管理系统。

   ```Shell
   (venv)$ python manage.py runserver
   ```
   