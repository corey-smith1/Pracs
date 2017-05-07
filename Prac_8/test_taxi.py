from taxi import Taxi
from taxi import UnreliableCar
from taxi import SilverServiceTaxi


def main():
    prius1 = Taxi('Prius 1', 100)
    prius1.drive(40)
    print(prius1)

#    prius1.drive(100)
#    print('{} and you fare is ${}'.format(prius1, prius1.get_fare()))

#    dodgcar1 = UnreliableCar('Dodgey Car 1',100,30)
#    dodgcar1.drive(65)
#    print(dodgcar1.__str__())

    silver = SilverServiceTaxi('fancyshit',100,2)
    silver.drive(10)
    print(silver.price_per_km)
    print(silver)


main()
