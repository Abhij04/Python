p1="Make alot of money"
p2="Buy now"
p3="Subscribe this"
p4="click this"

message =input("Enter your comment :")

if ((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
 print("this comment is a spam")

else:
 print("this comment is not a spam")