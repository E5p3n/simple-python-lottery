from flask import Flask, Response, request, jsonify
import os
import random

app = Flask(__name__)

player_tickets = []

test_tickets = ["cat", "cat", "dog", "dog", "fish", "fish", "bird"]

empty_msg = "There are no active tickets"
listerror_msg = "There was a problem with the list"
list_msg = "These are the currently active tickets"
ticketerror_msg = """To register type:
 `/spl_get [name] [number of tickets]`
 Without brackets, `[name]` is optional.
 Here's an example:
 `/spl_get Bob 3`
 """
confirmed_msg = "Tickets registered"
winner_msg = "The lucky winner is"
reset_msg = "All tickets have been destroyed"
help_msg = """*\"Simple Python Lottery\"*\n
\n
Commands:\n
\t`/spl_list` see currently active tickets.\n
\t`/spl_get [name] [number of tickets]` register tickets.\n
\t If you don't provide a name, then your username will be used.\n
\t`/spl_draw` get a winner.\n
\t`/spl_reset` delete *ALL* tickets.\n
\t`/spl_help` see this message again.\n
\n
\n_Version: 2.3_
"""
testactive_msg = "Test entries added to list"

# Command for checking currently active tickets
@app.route('/spl_list', methods=['POST'])
def spl_list():
    try:
        counted_tickets = []
        if not player_tickets:
            return jsonify(
                response_type='in_channel',
                text="%s." % empty_msg,
            )
        for x in set(player_tickets):
            counted = x,player_tickets.count(x)
            counted_tickets.append(counted)
        if counted_tickets != 0:
            return_list = '\t'.join(str(x)for x in counted_tickets)
            return jsonify(
                response_type='in_channel',
                text="%s" % return_list,
            )
    except ValueError:
        return "%s." % listerror_msg
    else:
        return jsonify(
            response_type='in_channel',
            text="%s:%s" % (list_msg, player_tickets),
        )

# Command for registering tickets
@app.route('/spl_get', methods=['POST'])
def spl_signup():
    try:
        text = request.form.get('text')
        username = request.form.get('user_name')
        input_list = text.split()
        if len(input_list) != 1 and len(input_list) != 2:
            return "%s" % ticketerror_msg
        if len(input_list) == 1:
            number = input_list.pop()
            num = int(number)
            nam = username
        if len(input_list) == 2:
            number = input_list.pop()
            num = int(number)
            name = input_list.pop()
            nam = name
        for x in range(0, num):
            player_tickets.append(nam)
        return jsonify(
            response_type='in_channel',
            text="%s: %s" % (confirmed_msg, num),
        )
    except (IndexError, ValueError):
            return "%s" % ticketerror_msg
    else:
            return "%s" % ticketerror_msg

# Command for drawing a winner
@app.route('/spl_draw', methods=['POST'])
def spl_draw():
    random.shuffle(player_tickets)
    try:
        winner = player_tickets.pop()
        return jsonify(
            response_type='in_channel',
            text="%s: %s" % (winner_msg, winner),
        )
    except IndexError:
        return jsonify(
            response_type='in_channel',
            text="%s." % empty_msg,
        )

# Command for deleting all active tickets
@app.route('/spl_reset', methods=['POST'])
def spl_reset():
    player_tickets[:] = []
    return jsonify(
        response_type='in_channel',
        text="*%s.*" % reset_msg,
    )

# Command for getting info about SPL
@app.route('/spl_help', methods=['POST'])
def spl_help():
    return jsonify(
        response_type='in_channel',
        text="%s" % help_msg,
    )

# Command for adding test entries into player_tickets
@app.route('/spl_test', methods=['POST'])
def spl_test():
    player_tickets.extend(test_tickets)
    return jsonify(
        response_type='in_channel',
        text="%s." % testactive_msg,
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port, debug=True)
