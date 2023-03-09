# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

print('################ PART 1 #####################')


def greet(name, greeting='Hello, <name>!'):
    output = greeting.replace("<name>", name)
    return output


print(greet('Doc'))
print(greet('Bob'))
print(greet('Bob', 'YO, <name>!'))

print('################ PART 2 #####################')


def force(mass=0.1, body='earth'):
    Surface_Gravity = dict(
        sun=274,
        jupiter=24.9,
        neptune=11.2,
        saturn=10.4,
        earth=9.8,
        uranus=8.9,
        venus=8.9,
        mars=3.7,
        mercury=3.7,
        moon=1.6,
        pluto=0.6)
    g = Surface_Gravity[body]
    force = mass * g
    return force


print(force())
print(force(5, 'pluto'))


print('################ PART 3 #####################')


def pull(m1, m2, d):
    G = 6.674*10**-11
    pull = G * ((m1*m2)/d**2)
    return pull


print(pull(800, 1500, 3))
