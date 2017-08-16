from flask import Blueprint, render_template
from . import itemslist_blueprint
from flask import render_template,session, redirect, request, url_for, flash

from ..decorators import login_required


@itemslist_blueprint.route('/shoppingList')
def itemsList():
    return render_template('shoppingList/index.html')


