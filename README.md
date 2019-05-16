# a2gapi-python

<p>Sample that shows how to connect with Alert2Gain's API with Python code.</p>

<b>Welcome!</b>
<p>This code is meant to be used to connect from Python with Alert2Gain's API for InputStreams. This code simulates a weather station that generates random values for probes related to temperature and humidity, for every simulated reading a timestamp is generated and formatted. </p>

<p>After the data is captured, it's sent to the API by the <b>sendData</b> method, when you set up the REST Request, you must send the x-api-key header that was assigned to your account in order to connect successfully.</p>

<b>Usage</b>
<p>Replace <b>[YOUR_API_KEY]</b> with the API Key provided by Alert2Gain, and replace <b>[YOUR_INPUTSTREAM_KEY]</b> with the Input Stream Key that was provided when you created the InputStream.</p>

<p>After your sample data is sent to the API, you can run the schema scanner tool that will run over the transmitted data in order to detect the schema of the transmitted data</p>

<b>Questions</b>
<p>You can submit an issue in this repo or write us back through the Alert2Gain contact email hello@alert2gain.com.</p>
