# Xray Classifier
Classify different disease based on Xrays! It currently classifies Covid 19, pneumonia and normal lungs with an accurracy of 93.3%

<h3> Installing Required Dependencies </h3>
<p>First of all install all the required dependencies with <br><code>pip install -r requirements.txt </code></p>

<h1> User Guide </h1>

<b><i> Please read this guide before using this repository. Otherwis errors might occurr! </i></b>

<ol>

<li>
<h2> Installing the Model </h2>
<p> The trained model was too big to be uploaded on Github. So, I decided to upload in on Google Drive from where you can acccess it </p>
<p> In future when the new/updated models will be trained, the link to them will be included in this file along with the instructions on how to use it </p>
<hr>
<p> So first of all download the model from  <a href="https://drive.google.com/file/d/1KBKUyLmSb7fHo5_uhpFZvi9661hEF4f8/view?usp=sharing"> this link </a></p>
<p> After downloading the <code>LossOptimized.zip</code> file extrat its content to <code>Classifier\trained_models</code> in the project's directory.</p>
<p> Your model should now be available at the following location </p>
<code> xray-classifier\Classifier\trained_models\LossOptimized </code>

<b>Don't rename the <code> LossOptimized </code> to anything else otherwise the webapp will give errors!</b>

</li>
<li>
<h2> Using Twitter Bot </h2>
<b><i> Follow the steps to setup twitter bot : </i></b>
<ul>
<li> Create a twitter developer accounts and get your keys (Consumer key, Consumer_secret, access token , access token secret). You can follow <a href="https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api"> this guide</a> </li>
<li>
Now open twitter_bot.py and fill the required fields with your keys
</li>
<li>
Make sure that Machine Learning model is available at <code>Classifier\\trained_models\\LossOptimized</code>
</li>

<li>
Open your twitter account and post a tweet like this <code>@XrayBotML checkxray</code> along with an x ray of lungs! <br>
<b><i>You can change the command <code>@XrayBotML checkxray</code> in the bot file (Open twitter_bot.py and read comments to see how to change it)</i></b>

</li>
<li>
Run the file locally and you will see your bot replying to the tweet!
</li>

</ul>
</li>
<li>
<h2>Add Django SECRET_KEY </h2>
<p>
Every django app needs a security key to work & when you create a django app by using command line interface it ccomes up with a security key!
But because this project is public. So, to prevent you guys from hacking (incase you deployed the app using the same security key) I removed the SECRET_KEY!
Here is how to generate a security key for your app!
<ol>
<li>
In the shell type <code> django-admin shell </code>
</li>
<li>
Now enter the following code <br> <code>
from django.core.management.utils import get_random_secret_key</code><br>
<code>
get_random_secret_key() </code>
<br><br>
It will give an output like this 
<code>
'h9&0svk92@fl&=&^)&)02j!#3zqzset%#)e)w9hbarwzvmdapy'
</code>

In django's settings.py specify it as follow:
<code>
SECRET_KEY = "Your random key here"
</code></li></ol></p></li>

<li>
<h2> RunServer </h2>
<p>
Now finally, you are all set up! And you can simply start your server by following these simple steps.
<ol>
<li>
Open your terminal and navigate to cloned repository
</li>
<li>
<p>Enter <code>python manage.py runserver</code> <b>command</b> and a local server will be started at <code>127.0.0.1:8000</code> Here you dhould see a homepage like this:</p>
<img src="https://user-images.githubusercontent.com/87518251/184303955-8cb066f7-f248-4617-987c-21a8461a8c68.png" alt="Doctor Robo X ray classifier home page">

</li>
<li>
<p>To check xray click on the <b> Check X ray button </b> and you will see a page like this!</p> <br>
<img src="https://user-images.githubusercontent.com/87518251/184304628-d28f57a5-a373-46f6-945c-8b654555cd5e.png" alt="Doctor robo check x ray">
</li>

<li>
<p>
Give your image file a name and <b> upload the file </b> using the <b>choose file</b> button then <b>click upload</b> </p>
<p><b><i> If you only want to test there are some sample x ray files in the media folder, you can use one of them </i></b><p><br>
<img src="https://user-images.githubusercontent.com/87518251/184305338-904115e2-08fd-4013-b9d2-32e46277ba00.png" alt="choose a file">
</li>

<li>
<p>After choosing the file <b><i>Click the upload button</i></b> The file will then be passed to the ML model you downloaded earlier. The Model will then process the file and will present you with a result of Xray! </p><br>
<p>
The result will look like this: <br> </p>
<img src="https://user-images.githubusercontent.com/87518251/184306352-c3fa93bc-8991-4e00-b257-e75fd44b0c4c.png">

</li>

</ol>
</p>
</li>
</ol>
