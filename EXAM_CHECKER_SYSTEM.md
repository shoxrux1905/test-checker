# Exam Checker System - Django Models

## System Overview

This is an exam checking system designed for teachers and students to manage assignments and exams. The system includes AI-powered checking capabilities and provides feedback to both students and teachers.

## Key Features

1. **Teachers** can create homework and exam questions in the system
2. **Students** can work on assignments and exams assigned to their group or individually
3. **AI-powered checking** of submitted assignments
4. **Group feedback** for teachers on class performance
5. **Student notifications** about assignment results
6. **Admin management** of groups, students, and teachers
7. **Multiple question types**: test, file upload, text answer, code writing

## Models Structure

### Users App (`apps.users.models`)

#### User Model

- **Purpose**: Extended Django user model with role-based access
- **Roles**: Admin, Student, Teacher
- **Key Fields**:
  - `role`: User role (admin/student/teacher)
  - `phone_number`: Contact information
  - `profile_picture`: User avatar
  - `created_at`, `updated_at`: Timestamps

### Assignments App (`apps.assignments.models`)

#### Group Model

- **Purpose**: Class/group management
- **Key Fields**:
  - `name`: Group name
  - `description`: Group description
  - `teacher`: Assigned teacher (ForeignKey to User)
  - `students`: Many-to-many relationship with students
  - `is_active`: Group status

#### Question Model

- **Purpose**: Different types of questions
- **Question Types**:
  - `test`: Multiple choice questions
  - `file`: File upload questions
  - `text`: Text answer questions
  - `code`: Code writing questions
- **Key Fields**:
  - `title`: Question title
  - `description`: Question description
  - `question_type`: Type of question
  - `points`: Points for the question
  - `created_by`: Creator (ForeignKey to User)

#### Answer Model

- **Purpose**: Student responses to questions
- **Key Fields**:
  - `question`: Related question
  - `student`: Student who answered
  - `selected_option`: For test questions
  - `text_answer`: For text questions
  - `file_answer`: For file questions
  - `code_answer`: For code questions
  - `is_correct`: Correctness status
  - `points_earned`: Points awarded
  - `feedback`: Feedback on the answer

#### Assignment Model

- **Purpose**: Exams and homework assignments
- **Assignment Types**: exam, homework
- **Key Fields**:
  - `title`: Assignment title
  - `description`: Assignment description
  - `assignment_type`: Type (exam/homework)
  - `group`: Assigned group
  - `questions`: Questions in the assignment
  - `start_time`, `end_time`: Assignment timing
  - `duration_minutes`: Time limit
  - `total_points`: Total possible points
  - `passing_score`: Minimum passing score
  - `max_attempts`: Maximum attempts allowed
  - `allow_late_submission`: Late submission policy

#### TestSession Model

- **Purpose**: Track exam sessions
- **Key Fields**:
  - `student`: Student taking the test
  - `assignment`: Related assignment
  - `session_token`: Unique session identifier
  - `started_at`, `ended_at`: Session timing
  - `is_active`: Session status
  - `ip_address`: Security tracking

#### Submission Model

- **Purpose**: Student submissions
- **Key Fields**:
  - `student`: Student who submitted
  - `assignment`: Related assignment
  - `test_session`: Related test session
  - `status`: Submission status (in_progress/submitted/graded)
  - `total_score`: Total score earned
  - `percentage_score`: Percentage score
  - `is_passed`: Pass/fail status
  - `ai_feedback`: AI-generated feedback
  - `ai_score`: AI-generated score

#### Result Model

- **Purpose**: Final grading results
- **Key Fields**:
  - `submission`: Related submission
  - `graded_by`: Teacher who graded
  - `final_score`: Final score
  - `feedback`: Teacher feedback
  - `is_final`: Final grade status

#### Appeal Model

- **Purpose**: Grade appeals by students
- **Appeal Status**: pending, under_review, approved, rejected
- **Key Fields**:
  - `student`: Student making appeal
  - `submission`: Related submission
  - `reason`: Appeal reason
  - `status`: Appeal status
  - `reviewed_by`: Teacher reviewing
  - `review_notes`: Review notes

### Common App (`apps.common.models`)

#### Notification Model

- **Purpose**: System notifications
- **Notification Types**:
  - assignment_created
  - assignment_due
  - grade_available
  - appeal_status
  - group_invitation
- **Key Fields**:
  - `recipient`: Notification recipient
  - `notification_type`: Type of notification
  - `title`: Notification title
  - `message`: Notification message
  - `is_read`: Read status

#### TestOption Model

- **Purpose**: Multiple choice options
- **Key Fields**:
  - `question`: Related question
  - `option_text`: Option text
  - `is_correct`: Correct option flag
  - `order`: Option order

#### GroupFeedback Model

- **Purpose**: Group performance feedback
- **Key Fields**:
  - `group`: Related group
  - `assignment`: Related assignment
  - `feedback_text`: Feedback content
  - `average_score`: Group average score
  - `total_submissions`: Total submissions count
  - `passed_count`: Passed submissions count

## API Endpoints Structure

Based on the requirements, the system will have these API endpoints:

### User Management

- `POST /api/users/register/` - User registration
- `POST /api/users/login/` - User login
- `PUT /api/users/update/` - User profile update

### Group Management

- `POST /api/groups/create/` - Create group
- `PUT /api/groups/{id}/update/` - Update group
- `POST /api/groups/{id}/archive/` - Archive group

### Question Management

- `POST /api/questions/create/` - Create question
- `PUT /api/questions/{id}/update/` - Update question
- `DELETE /api/questions/{id}/delete/` - Delete question
- `GET /api/questions/{id}/read/` - Read question

### Answer Management

- `POST /api/answers/create/` - Create answer
- `PUT /api/answers/{id}/update/` - Update answer
- `DELETE /api/answers/{id}/delete/` - Delete answer
- `GET /api/answers/{id}/read/` - Read answer

### Assignment Management

- `POST /api/assignments/create/` - Create assignment
- `PUT /api/assignments/{id}/update/` - Update assignment
- `DELETE /api/assignments/{id}/delete/` - Delete assignment
- `GET /api/assignments/{id}/read/` - Read assignment

### Submission Management

- `POST /api/submissions/create/` - Create submission
- `GET /api/submissions/{id}/read/` - Read submission

### Result Management

- `GET /api/results/{id}/read/` - Read result
- `PUT /api/results/{id}/update/` - Update result

### Appeal Management

- `POST /api/appeals/create/` - Create appeal
- `GET /api/appeals/{id}/read/` - Read appeal
- `PUT /api/appeals/{id}/update/` - Update appeal

### Student Endpoints

- `GET /api/students/my-submissions/` - My submissions
- `GET /api/students/my-assignments/` - My assignments

### Teacher Endpoints

- `GET /api/teachers/my-groups/` - My groups
- `GET /api/teachers/my-students/` - My students
- `GET /api/teachers/my-assignments/` - My assignments
- `GET /api/teachers/appeals/` - Appeal list

## Database Relationships

### Core Relationships

- **User** → **Group** (Teacher: One-to-Many, Student: Many-to-Many)
- **Group** → **Assignment** (One-to-Many)
- **Assignment** → **Question** (Many-to-Many)
- **Question** → **Answer** (One-to-Many)
- **Assignment** → **Submission** (One-to-Many)
- **Submission** → **Result** (One-to-One)
- **Submission** → **Appeal** (One-to-Many)

### Supporting Relationships

- **Question** → **TestOption** (One-to-Many)
- **User** → **Notification** (One-to-Many)
- **Group** → **GroupFeedback** (One-to-Many)

## Usage Examples

### Creating a Group

```python
# Create a group
group = Group.objects.create(
    name="Computer Science 101",
    description="Introduction to Computer Science",
    teacher=teacher_user
)

# Add students to group
group.students.add(student1, student2, student3)
```

### Creating Questions

```python
# Create a test question
test_question = Question.objects.create(
    title="What is Python?",
    description="Choose the correct definition of Python",
    question_type="test",
    points=5,
    created_by=teacher_user
)

# Add test options
TestOption.objects.create(
    question=test_question,
    option_text="A programming language",
    is_correct=True,
    order=1
)

# Create a text question
text_question = Question.objects.create(
    title="Explain recursion",
    description="Write a brief explanation of recursion",
    question_type="text",
    points=10,
    created_by=teacher_user
)
```

### Creating an Assignment

```python
# Create an assignment
assignment = Assignment.objects.create(
    title="Midterm Exam",
    description="Midterm examination for CS101",
    assignment_type="exam",
    group=group,
    created_by=teacher_user,
    start_time=datetime.now(),
    end_time=datetime.now() + timedelta(hours=2),
    duration_minutes=120,
    total_points=100,
    passing_score=60
)

# Add questions to assignment
assignment.questions.add(test_question, text_question)
```

### Student Submission

```python
# Create a submission
submission = Submission.objects.create(
    student=student_user,
    assignment=assignment,
    status="submitted",
    submitted_at=timezone.now(),
    total_score=85
)

# Create answers
Answer.objects.create(
    question=test_question,
    student=student_user,
    selected_option="A",
    is_correct=True,
    points_earned=5
)

Answer.objects.create(
    question=text_question,
    student=student_user,
    text_answer="Recursion is when a function calls itself...",
    points_earned=8
)
```

## Installation and Setup

1. **Install Dependencies**:

   ```bash
   pip install django djangorestframework
   ```

2. **Configure Settings**:

   - Set `AUTH_USER_MODEL = 'users.User'` in settings.py
   - Add apps to `INSTALLED_APPS`

3. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser**:

   ```bash
   python manage.py createsuperuser
   ```

5. **Start Development Server**:
   ```bash
   python manage.py runserver
   ```

## System Workflow

### Teacher Workflow

1. Create questions (test, file, text, code)
2. Create groups and add students
3. Create assignments with questions
4. Review submissions and provide feedback
5. Handle appeals from students

### Student Workflow

1. Join groups assigned by teacher
2. View assigned assignments
3. Take exams or complete homework
4. Submit answers
5. Receive notifications about results
6. Appeal grades if needed

### Admin Workflow

1. Manage users (students, teachers)
2. Create and manage groups
3. Assign teachers to groups
4. Monitor system usage
5. Handle system-wide issues

## Security Features

- **Role-based access control** for different user types
- **Session tracking** for exam security
- **IP address logging** for audit trails
- **Time-based access control** for assignments
- **Attempt limiting** to prevent abuse
- **File upload security** for file-based questions

## AI Integration Points

The system is designed to integrate with AI services for:

- **Automatic grading** of text and code answers
- **Feedback generation** for student submissions
- **Plagiarism detection** for submitted content
- **Performance analytics** for group insights

This exam checker system provides a comprehensive solution for educational assessment with modern features like AI integration, real-time notifications, and flexible question types.
