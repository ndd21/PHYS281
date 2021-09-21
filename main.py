"""
Mkdocs macro for a counter.
"""

def define_env(env):
    env.variables["excount"] = 0
    env.variables["adexcount"] = 0

    @env.macro
    def counter():
        env.variables["excount"] += 1
        return env.variables["excount"]

    @env.macro
    def advcounter():
        env.variables["adexcount"] += 1
        return env.variables["adexcount"]
