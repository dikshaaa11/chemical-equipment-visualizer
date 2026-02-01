Skip to content
dikshaaa11
chemical-equipment-visualizer
Repository navigation
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
chemical-equipment-visualizer
/
README.md
in
main

Edit

Preview
Indent mode

Spaces
Indent size

2
Line wrap mode

Soft wrap
Editing README.md file contents
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148

### Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```
Backend runs at:

http://127.0.0.1:8000

Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

http://localhost:5173

 Authentication

Login uses JWT (/api/token/)

Access token is stored in browser localStorage

Protected endpoints:

CSV upload

Upload history

PDF download

PDF Reports

PDF reports are generated automatically after a successful CSV upload

Reports are stored temporarily on the backend

Users can securely download the report after authentication

Media files are not committed to GitHub

 Git & Repository Notes

node_modules/, media files, and binaries are excluded via .gitignore

No files larger than GitHub’s size limits are tracked

Repository contains only clean source code and sample data

 Sample Data

A sample CSV file is included:

sample_data/sample_equipment_data.csv


Use this to test uploads immediately after setup.
Use Control + Shift + m to toggle the tab key moving focus. Alternatively, use esc then tab to move to the next interactive element on the page.
No file chosen
Attach files by dragging & dropping, selecting or pasting them.
