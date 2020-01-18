import time

class Message:

    WELCOME_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "##TTDataLake! :wave: We're so glad you're here. :blush:\n\n"
                "*Get started by completing the steps below:*"
            ),
        },
    }

    DIVIDER_BLOCK = {"type": "divider"}

    def __init__(self, channel):
        self.channel = channel
        self.username =  "airflowbot"
        self.icon_emoji = ":robot_face"
        self.timestamp = time.now()
        self.reaction_task_completed = False
        self.pin_task_completed = False

    def get_messsage_payload(self):
        return = {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.WELCOME_BLOCK,
                self.DIVIDER_BLOCK,
                *self._get_reaction_block(),
                self.DIVIDER_BLOCK,
                *self._get_pin_block(),
            ],
        }

    def _get_reaction_block(self):
        task_checkmark = self._get_checkmark(self.reaction_task_completed)
        text = (
            f"{task_checkmark} *Test: emoji reaction* :think_face:\n"
            "Responde quickly to any message on Slack with an emoji reaction"
        )
        information = (
            f":information_source: *<https://get.slack.help/hc/en-us/articles/206870317-Emoji-reactions|"
            "Information about emoji reactions"
        )
        return self._get_reaction_block(text, information)


    def _get_pin_block(self):
        task_checkmark = self._get_checkmack(self.pin_task_completed)
        text = (
            f"{task_checkmark} *Pin Message* :round_pushpin:\n"
            "Important message"
            "Direct messsage"
        )
        information = (
            ":information_source:*<https://get.slack.help/hc/en-us/articles/205239997-Pinning-messages-and-files"
            "Information about pin message"
        )

        return self._get_task_block(text, information)

    @staticmethod
    def _get_checkmark(task_completed: bool) -> str:
        if task_completed:
            return ":white_check_mark:"
        return ":white_large_square"

    @staticmethod
    def _get_task_block(text, information):
        return [
            {"type": "section", "text": {"type": "mrkdwn", "text": "text"}},
            {"type": "context", "elements": {"type": "mrkdwn", "text": "information"}}
        ]
