=================
Hotel Reservation
=================

Project Setup
-------------
1. ``git clone https://github.com/delsananthony/hotel-reservation.git``
2. Install Poetry_ and run ``poetry install``.

  .. _Poetry: https://python-poetry.org/docs/#installing-with-the-official-installer/
   .. |target| replace:: _blank

3. Run command, ``poetry run python manage.py runserver``

Documentation
~~~~~~~~~~~~~
[1.] Models
    a. Customer
        - name
        - contact_no
        - address
        - birth_date
        - age
    b. RoomCategory
        - name
        - description
        - active
    c. Room
        - name
        - room_categ > RoomCategory
        - state ['occupied', 'vacant', 'maintenance']
        - package_rate
        - hourly_rate
        - active
    d. Reservation
        - customer > Customer
        - room > Room
        - reservation_date
        - note
    e. CheckingDuration
        - hours
        - time_from
        - time_to
        - active
    f. CheckingTransaction
        - reservation > Reservation
        - type ['walk_in', 'with_reservation']
        - customer > Customer
        - room > Room
        > check_in()
        > check_out()
        > check_term()
        > check_extend()
        > make_payment()
    f. CheckingTerm
        - check_trans > CheckingTransaction
        - check_duration > CheckingDuration
        - status ['unpaid', 'paid', 'check_in', 'check_out']
        - date_checked_in
        - date_check_out
        - active
        > get_check_term()
        > paid()
        > check_in()
        > check_out()
    g. Payment
        - check_trans > CheckingTransaction
        - check_term > CheckingTerm
        - amount
        - date_paid
    h. Journal
        - name
        - code
        - type
        - default_debit_account
        - default_credit_account
    i. Account
        - name
        - type
    j. AccountLine
        - account > Account
        - label
        - date
        - debit
        - credit
    k. Entry
        - journal > Journal
        - date
        > reconcile()
        > unreconcile()
        > post()
    l. EntryLine
        - account_line > AccountLine
        - is_posted
        - is_reconciled


