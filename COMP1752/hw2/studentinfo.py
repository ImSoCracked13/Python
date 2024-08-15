import database01 as db

names = db.get_names()
user_ids = db.get_user_ids()
infos = db.get_infos()


def user_info(name, user_id, info):
    for i in range(len(names)):
        name = names[i]
        user_id = user_ids[i]
        info = infos[i]
        print(f"name:      {name}")
        if user_id is not None:
            print(f"user id:   {user_id}")
        if info is not None:
            if info.startswith("BSc ") or info.startswith("MSc "):  
                print(f"programme: {info}")
            else:  
                print(f"job title: {info}")
        print()



def search():
    x = input("Enter username: ")
    for i in range(len(names)):
        if x == names[i]:
            print(names[i])
            print(user_ids[i])
            print(infos[i])


def is_send(info, group):
    send_message = False
    if group == "all":
        send_message = True
    elif info is not None:
        is_student = info.startswith("BSc ") or info.startswith("MSc ")
        if group == "students" and is_student:
            send_message = True
        if group == "staff" and not is_student:
            send_message = True
    return send_message

def send_message(names, infos):
    while True:
        group = input("Group (staff, students or all)? ")
        if group == "":
            break
        message = input("Message? ")
        if message == "":
            break
        for i in range(len(infos)):
            info = infos[i]
            send_message = is_send(group, info)
            if send_message:
                name = names[i]
                print(f" '{message}' sent to {name}")





user_info(names, user_ids, infos)
search()
send_message(names, infos)