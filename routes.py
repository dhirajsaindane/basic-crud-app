from flask import Blueprint, render_template, request, redirect, url_for, flash
from extensions import db
from models import Employee, Department

main = Blueprint('main', __name__)

@main.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@main.route('/add', methods=['GET', 'POST'])
def add_employee():
    departments = Department.query.all()
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department_id = request.form['department']

        new_emp = Employee(name=name, email=email, department_id=department_id)
        db.session.add(new_emp)
        db.session.commit()
        flash("Employee added successfully!", "success")
        return redirect(url_for('main.index'))
    return render_template('add_employee.html', departments=departments)

@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    emp = Employee.query.get_or_404(id)
    departments = Department.query.all()
    if request.method == 'POST':
        emp.name = request.form['name']
        emp.email = request.form['email']
        emp.department_id = request.form['department']
        db.session.commit()
        flash("Employee updated successfully!", "info")
        return redirect(url_for('main.index'))
    return render_template('edit_employee.html', employee=emp, departments=departments)

@main.route('/delete/<int:id>')
def delete_employee(id):
    emp = Employee.query.get_or_404(id)
    db.session.delete(emp)
    db.session.commit()
    flash("Employee deleted successfully!", "danger")
    return redirect(url_for('main.index'))

# --- Department Routes ---

@main.route('/departments')
def list_departments():
    departments = Department.query.all()
    return render_template('departments.html', departments=departments)

@main.route('/departments/add', methods=['POST'])
def add_department():
    name = request.form['name']
    if Department.query.filter_by(name=name).first():
        flash("Department already exists!", "warning")
    else:
        dept = Department(name=name)
        db.session.add(dept)
        db.session.commit()
        flash("Department added successfully!", "success")
    return redirect(url_for('main.list_departments'))
