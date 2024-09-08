// Implementation of bank account simple credit, debit and balance check.
class Account {
    bank = "SBI"
    branch = "Hyderabad"
    acc_count = 0
    constructor(acc_no, name, bal=500){
        this.acc_no = acc_no;
        this.name = name;
        this.bal = bal;
        Account.acc_count += 1;
    }

    displayInfo(){
        console.log(`${this.acc_no}: ${this.name}: having balance ${this.bal}`);
    }

    credit(amt){
        this.bal += amt;
        return this.bal;
    }

    debit(amt){
        if (500 < this.bal - amt){
            this.bal -= amt;
            return this.bal;
        } else {
            return "Insuffient balance.";
        }
    }

    get_balance(){
        console.log(`Your balance amount: ${this.bal}`);
    }
}


navn = new Account(234, 'Naveen', 10000);
navn.displayInfo();
navn.credit(4000);
navn.get_balance();
navn.debit(2000);
navn.get_balance();



