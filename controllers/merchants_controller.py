from flask import Flask, render_template, request, redirect
from repositories import merchant_repository
from models.merchant import Merchant
from models.functions import total_spend
from flask import Blueprint

merchants_blueprint = Blueprint("merchants",__name__)

@merchants_blueprint.route("/merchants")
def merchants():
    merchants = merchant_repository.select_all()
    return render_template("merchants/index.html", all_merchants = merchants)



@merchants_blueprint.route("/merchants", methods = ["POST"])
def create_merchant():
    name = request.form['name']
    category = request.form['category']
    active = request.form['active']
    merchant = Merchant(name, category, active)
    merchant_repository.save(merchant)
    return redirect('/merchants')

@merchants_blueprint.route("/merchant/<id>/edit")
def edit_merchant(id):
    merchant = merchant_repository.select(id)
    return render_template("merchants/edit.html", merchant=merchant)

@merchants_blueprint.route("/merchant/<id>/edit_complete", methods = ['POST'])
def update_merchant(id):
    name = request.form['name']
    category = request.form['category']
    active= request.form['active']
    merchant = Merchant(name, category, active, id)
    merchant_repository.update(merchant)
    return redirect('/merchants')


@merchants_blueprint.route("/merchants/<id>/delete", methods = ["POST"])
def delete_merchant(id):
    merchant_repository.delete(id)
    return redirect('/merchants')

@merchants_blueprint.route("/merchant/<id>/transactions")
def merchant_transactions(id):
    transactions = merchant_repository.transactions(id)
    total= total_spend(transactions)
    return render_template("merchants/transactions.html", transactions=transactions, total=total)
