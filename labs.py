

# an list of state dictionaries
states = [

{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]


def find_state(state):

    for i in range(0, len(states)):
        if state == states[i]['name']:
            print(f"state: {states[i]['name']} @: {i}")
            return i 

# this funciton adds the new key to the list and return the modified list
def add_tries(s=None,wrg=None):
 
        
        for i in range (0, len(states)):

            if wrg == None:

                if s == states[i]['name']:
                    
                    # print(f" Found state: {states[i]['name']} on index {i}")
                    try:
                        
                        # print(states[i]['tries'])
                        states[find_state(s)]['correctTries'] += 1

                    except KeyError: #if the key doesn't exist 
                        print(f"ERROR: {KeyError}  catch")
                        # create the new key and add the value
                        newKey = "correctTries"
                        newValue = 1
                        states[i][newKey] = newValue
                    
                        return states
            else:
                 
                if s == states[i]['name']:
                    
                    # print(f" Found state: {states[i]['name']} on index {i}")
                    try:
                        
                        # print(states[i]['tries'])
                        states[find_state(s)]['wrongTries'] += 1
 
                    except KeyError: #if the key doesn't exist 
                        print(f"ERROR: {KeyError}  catch")
                        # create the new key and add the value
                        newKey = "wrongTries"
                        newValue = 1
                        states[i][newKey] = newValue
                    
                        return states


        #    if s == state['name'] :
        #        print(f"found the state: {state['name']}")

        # state = states.get(s)
        # states[s]

        # return state

def question():
    for state in states:
        # print(states[find_state(state['name'])]['capital'])
        # print(state)
        userInput = input(f" what's the Capital of {state['name']}: ")

        if str(userInput) == states[find_state(state['name'])]['capital']:

            print("correct")

        else:
            print("WRONG!!!")


playing = True
def start_game():
    while(playing == True):
    
        question()





start_game()

# find_state('Florida')
# print(new_states)
# print(f'{new_states} THE NEW STATES')
 
# print(add_tries(1,'Alabama'))
# for state in states:

#            if s == state['name'] :
#                print(f"found the state: {state['name']}")