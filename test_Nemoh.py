#!/usr/bin/env python
# coding: utf-8

import numpy as np
from bodies import *
from problems import RadiationProblem
from Nemoh import *

def test_floatting_sphere():
    sphere = Sphere(radius=1.0, ntheta=7, nphi=7, clip_free_surface=True)
    sphere.dof["Heave"] = sphere.faces_normals @ (0, 0, 1)
    problem = RadiationProblem(bodies=[sphere], omega=1.0, depth=np.infty)
    solver = Nemoh()
    mass, damping = solver.solve(problem)
    assert np.isclose(mass, 1819.6, rtol=1e-4)
    assert np.isclose(damping, 379.39, rtol=1e-4)

def test_floatting_sphere_finite_depth():
    sphere = Sphere(radius=1.0, ntheta=7, nphi=7, clip_free_surface=True)
    sphere.dof["Heave"] = sphere.faces_normals @ (0, 0, 1)
    problem = RadiationProblem(bodies=[sphere], omega=1.0, depth=10.0)
    solver = Nemoh()
    mass, damping = solver.solve(problem)
    assert np.isclose(mass, 1740.6, rtol=1e-4)
    assert np.isclose(damping, 380.46, rtol=1e-4)

def test_alien_sphere():
    sphere = Sphere(radius=1.0, ntheta=7, nphi=7, clip_free_surface=True)
    sphere.dof["Heave"] = sphere.faces_normals @ (0, 0, 1)
    problem = RadiationProblem(bodies=[sphere], rho=450.0, g=1.625, omega=1.0, depth=np.infty)
    solver = Nemoh()
    mass, damping = solver.solve(problem)
    assert np.isclose(mass, 515, rtol=1e-3)
    assert np.isclose(damping, 309, rtol=1e-3)