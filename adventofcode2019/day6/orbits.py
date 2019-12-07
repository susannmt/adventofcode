
class Obj:
    orbits: list
    def __init__(self, name):
        self.name = name
        self.orbitted_by_list = []
        self.orbits_list = []

    def orbitted_by(self, other_obj):
        self.orbitted_by_list.append(other_obj)
        other_obj.orbits_list.append(self)


def collect_orbit_objects(thing: Obj, level: int):
    global direct_counter
    global indirect_counter

    if not thing.orbitted_by_list:
        return

    for orbits in thing.orbitted_by_list:
        collect_orbit_objects(orbits, level+1)
        direct_counter += 1
        indirect_counter += level

if __name__ == '__main__':
    orbit_map = [line.strip().split(")") for line in open("input.txt").readlines()]

    orbit_dict = {}
    direct_counter = 0
    indirect_counter = 0

    for center, thing in orbit_map:
        if center not in orbit_dict:
            orbit_dict[center] = Obj(center)
        if thing not in orbit_dict:
            orbit_dict[thing] = Obj(thing)

        orbit_dict[center].orbitted_by(orbit_dict[thing])

    collect_orbit_objects(orbit_dict["COM"], level=0)
    print(direct_counter + indirect_counter)

    santa_centers = []
    main = orbit_dict["SAN"]
    level = 0
    while main.orbits_list:
        level += 1
        main = main.orbits_list[0]
        santa_centers.append((main.name, level))


    your_centers = []
    main = orbit_dict["YOU"]
    level = 0
    while main.orbits_list:
        level += 1
        main = main.orbits_list[0]
        your_centers.append((main.name, level))

    for center, dist in santa_centers:
        for center2, dist2 in your_centers:
            if center == center2:
                print(center, dist+dist2-2)
