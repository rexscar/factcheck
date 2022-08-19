from twitivity import Event
import json

class StreamEvent(Event):
    CALLBACK_URL: str = "https://1f8c-196-11-90-118.eu.ngrok.io/listener"

    def on_data(self, data: json) -> None:
        print(data)
        # process data

stream_events = StreamEvent()
stream_events.listen()