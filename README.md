# PersonalCalendar
**Introduction**<br>
I developed a personal calendar use Python Flask and Html.<br>
You can click a day to edit your task today.<br>
​​​​It looks like this.<br>
![image](https://github.com/user-attachments/assets/ea3ccd20-ff3e-4a19-844a-bc2b4d6a19b2)
![image](https://github.com/user-attachments/assets/ad42bf81-0398-4905-ba15-f08efe7cb1e4)
**Install**<br>
pip install flask Pillow<br>
python app.py<br>
**Principle**<br>
I creat 30 file on static/task which storage task data<br>
Function create_calendar_with_task() will draw calendar,show today with blue. Then read that file and write task in calendar.<br>
If clicked in one day, js will show text editor and you can edit task. Then push save button to save task and redraw Calendar.png and reload the web page.<br>
**Use In Phone**<br>
![image](https://github.com/user-attachments/assets/d1c1f92d-9659-4e20-8672-1e095c533ede)
![image](https://github.com/user-attachments/assets/30d36871-1bb9-4f7b-988a-56b1ace4429b)
