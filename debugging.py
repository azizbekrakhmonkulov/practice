''' Packiges & Debugging
(1) Python packeges & Core Package
(2) Packege Manager & External Package
(3) Debugging
'''


from PIL import Image
import turtle
print("===== Python packeges & Core Package =====")
'''Python Packeges/Modules: Core File and External'''
# Core Packages > https://docs.python.org/3/library


# # Core package
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(1)
# t.circle(100)

# turtle.done()


my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()


# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("DONE")


print("===== Packege Manager & External Package =====")

'''Package Managers > pip, pipenv, npm, yarn, composer, brew'''
# Packege external > https://pypi.org/
with Image.open("material/zip.jpg") as img_obj:
    resize_img = img_obj.resize((200, 200))
    resize_img.show()
    resize_img.save("material/samle.png")
