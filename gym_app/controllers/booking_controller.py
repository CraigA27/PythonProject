from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.session_repository as session_repository
import repositories.member_repository as member_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("/bookings/index.html", bookings=bookings)

@bookings_blueprint.route("/bookings/<id>")
def show(id):
    booking = booking_repository.select(id)
    return render_template("/bookings/show.html", booking=booking)

@bookings_blueprint.route("/bookings/new")
def new_booking():
    sessions = session_repository.select_all_by_date()
    members = member_repository.select_all()
    return render_template("/bookings/new.html", sessions=sessions, members=members)

@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete(id):
    booking_repository.delete(id)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings",  methods=["POST"])
def add_booking():
    member_id = request.form["member_id"]
    session_id = request.form["session_id"]
    member = member_repository.select(member_id)
    session = session_repository.select(session_id)
    booking = Booking(member, session)
    booking_repository.save(booking)
    return redirect("/bookings")