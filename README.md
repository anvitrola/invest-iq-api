<div align="center">
    <img width="209" alt="mainImage" src="https://github.com/anvitrola/invest-iq-app/assets/62806299/61f91ab9-8593-4f1d-a825-0311bd0047a4">
    <h1>Invest IQ</h1>
    <p>Stay Informed, Make Informed Decisions</p>
    <p>
        <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">
            <img src="https://img.shields.io/badge/language-Python-blue" alt="Repo Main Language" />
        </a>
        <a href="https://your-invest-iq-app-url.com">
            <img src="https://img.shields.io/badge/platform-web-blueviolet" alt="Project Platform" />
        </a>
        <a href="https://github.com/your-username/your-repo/blob/main/LICENSE">
            <img src="https://img.shields.io/badge/license-MIT-red" alt="Repo License" />
        </a>
    </p>
</div>


## 📈📊 About the Project
<p>
    Invest IQ is a platform that helps you keep track of your stock investments. Set upper and lower price boundaries, create your stock portfolio, and receive email notifications when opportunities arise.
</p>
<p>
    Please note that this is a <b>simulated application</b> for educational purposes. No real financial transactions are involved.
</p>

<p>This is the back-end repository for the "Invest IQ" application, built with Python and Django. The back-end handles stock price monitoring, boundary tracking, and email notifications.
</p>

</div>

## 💻 Features

- **Stock Monitoring API**: The API allows you to monitor stock prices in real-time, set boundaries, and receive email notifications when trading opportunities arise.

## 🛠 Main Technologies
- [Python](https://docs.python.org/3/) 
- [Django](https://docs.djangoproject.com/en/4.2/) 
- [Celery](https://docs.celeryq.dev/en/stable/index.html)
- [Redis](https://redis.io/docs/)
- A code editor like [VSCode](https://code.visualstudio.com/)

### 🚀 Running the Project

1. Clone this repo
`git clone https://github.com/anvitrola/invest-iq-api.git`

2. Create a virtual environment:
`python -m venv venv`

3. Activate virtual environment:
`source venv/bin/activate`

4. Install the required dependencies:
`pip install -r requirements.txt`

5. Set up the database:
`python manage.py migrate`

6. Create a superuser which will alow you to login into Django Admin on localhost:800:
`python manage.py createsuperuser`

3. Start the development server:
`python manage.py runserver`


### Run the monitoring task

1. Activate Redis-server:
`redis-server`

2. Activate celery worker
`celery -A invest_iq worker --loglevel=info`

3. Activate celery beat (scheduler):
`celery -A invest_iq beat --loglevel=info`



<p>You can find the APP here -> <a href="https://github.com/anvitrola/invest-iq-app">here</a>. 🌸</p>


<div align="center">
  <h2>Open Source</h2>
    <h3>By  <a href="https://www.linkedin.com/in/anvitrola/">Ana Vitória Viana<a/></h3>
    <h3>Contributions are welcome! Please open a pull request for review.</h3>
  <sub>Copyright © 2023</sub>
  <p>Invest IQ <a href="[https://github.com/your-username/your-repo/blob/main/LICENSE](https://opensource.org/license/mit/)https://opensource.org/license/mit/">is MIT licensed 💖</a></p>
</div>