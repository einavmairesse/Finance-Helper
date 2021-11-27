from flask import request, Response, jsonify, Blueprint
from FinanceTracker.models import Expense, db

from FinanceTracker.services.date_utils import str_to_date


expenses_blueprint = Blueprint('expenses', __name__)


@expenses_blueprint.route('/expense', methods=['POST'])
def create_expense():
    data = request.json
    date = str_to_date(data['date'])

    new_expense = Expense(name=data['name'], amount=data['amount'], date=date)
    db.session.add(new_expense)
    db.session.commit()
    return Response("", status=201, mimetype='application/json')


@expenses_blueprint.route('/expense/list')
def index():
    expense = Expense.query.first()
    return get_response_from_expense(expense)


def get_response_from_expense(expense):
    return jsonify(name=expense.name, amount=expense.amount, date=expense.date)