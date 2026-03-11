#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ARS RERUM LABS: The Generative Engine
======================================
Implementation of the Binary Additive Sieve (Generative Search)

Classical mathematics uses the Sieve of Eratosthenes (Archaeology) - an algorithm
that assumes a closed phase space [1, N] and subtracts elements to find primes.
This script implements Generative Search (Architecture) - the system dynamically 
expands its phase space (dΩ/dt > 0) creating orthogonal dimensions (primes) 
whenever it encounters Ontological Pain (an unexplainable gap).

Author: Kajetan Młynarski (concept), Gemini & DeepSeek (implementation)
Date: March 2026
License: CC BY-NC 4.0
"""

class GenerativeAdditiveSieve:
    """
    A minimal implementation of generative search.
    
    The number line is treated as an open phase space Ω(t). When the current
    state is already covered by exploitation waves, the system interpolates.
    When it encounters a gap, it experiences Ontological Pain and bifurcates,
    creating a new orthogonal dimension and expanding |Ω|.
    """
    
    def __init__(self):
        self.orthogonal_dimensions = []  # List of primes (atoms)
        # Exploitation waves: next_multiple -> list of primes hitting it
        self.exploitation_waves = {}     
        self.current_state = 2           # Expanding frontier of phase space
        self.pain_count = 0               # Number of bifurcations
        self.total_states = 0             # Total states visited
        
    def step(self):
        """
        Executes one quantum of generative search along the number line.
        
        Returns:
            int or None: The new prime if bifurcation occurs, else None.
        """
        self.total_states += 1
        
        # 1. Check if current state is covered by existing waves
        if self.current_state in self.exploitation_waves:
            # Interpolation/Exploitation Phase: State is explainable by existing dimensions
            # Propagate waves forward (symmetric sums: p + p + ...)
            active_primes = self.exploitation_waves.pop(self.current_state)
            
            for p in active_primes:
                next_multiple = self.current_state + p
                if next_multiple not in self.exploitation_waves:
                    self.exploitation_waves[next_multiple] = []
                self.exploitation_waves[next_multiple].append(p)
                
            new_dimension = None

        else:
            # 2. Ontological Pain Detection (Gap encountered!)
            # The current state cannot be reduced to a symmetric sum of past elements.
            self.pain_count += 1
            
            # 3. Bifurcation: Generate a new orthogonal dimension
            new_dimension = self.current_state
            self.orthogonal_dimensions.append(new_dimension)
            
            # Initiate the exploitation wave for the new dimension
            next_multiple = new_dimension + new_dimension
            if next_multiple not in self.exploitation_waves:
                self.exploitation_waves[next_multiple] = []
            self.exploitation_waves[next_multiple].append(new_dimension)

        # Expand phase space frontier
        self.current_state += 1
        return new_dimension
    
    def get_statistics(self):
        """Return thermodynamic statistics of the generative process."""
        return {
            'dimensions': len(self.orthogonal_dimensions),
            'pain_events': self.pain_count,
            'total_states': self.total_states,
            'active_waves': len(self.exploitation_waves),
            'prime_density': len(self.orthogonal_dimensions) / self.total_states,
            'phase_space_volume': self.current_state,
        }


def visualize_waves(engine, limit=50):
    """
    Simple ASCII visualization of wave coverage.
    
    P = new prime (bifurcation point)
    1-9 = number of waves covering that state
    . = uncovered (should not exist after processing)
    """
    coverage = [0] * limit
    for target, primes in engine.exploitation_waves.items():
        if target < limit:
            coverage[target] = len(primes)
    
    print("\nWave coverage visualization:")
    for i in range(limit):
        if i in engine.orthogonal_dimensions:
            marker = 'P'
        elif coverage[i] > 0:
            marker = str(coverage[i] % 10)
        else:
            marker = '.'
        print(marker, end='')
        if (i+1) % 20 == 0:
            print()
    print()


def run_demonstration(steps=30, visualize=True):
    """
    Run the generative sieve and display results.
    """
    print("=" * 70)
    print("ARS RERUM: GENERATIVE SEARCH OPTIMIZATION (ADDITIVE SIEVE)")
    print("=" * 70)
    print("\nLegend:")
    print("  [State] | Event               | Active Waves (Coverage)")
    print("-" * 70)
    
    engine = GenerativeAdditiveSieve()
    
    for _ in range(steps):
        state = engine.current_state
        new_prime = engine.step()
        
        # Format active waves for display
        waves_list = [f"{t}({len(p)})" for t, p in sorted(engine.exploitation_waves.items())]
        waves_str = ", ".join(waves_list[:5])  # Show first 5 only
        if len(waves_list) > 5:
            waves_str += f"... (+{len(waves_list)-5})"
        
        if new_prime:
            print(f"[{state:<4}] | BIFURCATION: +{new_prime:<4} | {waves_str}")
        else:
            print(f"[{state:<4}] | Covered (Wave)       | {waves_str}")
    
    # Statistics
    stats = engine.get_statistics()
    print("\n" + "=" * 70)
    print("THERMODYNAMIC STATISTICS")
    print("=" * 70)
    print(f"Phase space volume (current state): {stats['phase_space_volume']}")
    print(f"New dimensions generated (primes): {stats['dimensions']}")
    print(f"Prime density: {stats['prime_density']:.3f}")
    print(f"Ontological Pain events: {stats['pain_events']}")
    print(f"Active exploitation waves: {stats['active_waves']}")
    
    if visualize:
        visualize_waves(engine, limit=stats['phase_space_volume'])


def test_sieve():
    """Unit test: verify first 15 primes."""
    engine = GenerativeAdditiveSieve()
    primes_found = []
    for _ in range(50):
        p = engine.step()
        if p:
            primes_found.append(p)
    
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert primes_found[:15] == expected_primes, f"Got {primes_found[:15]}, expected {expected_primes}"
    print("✓ Sieve generates correct prime sequence")
    return True


if __name__ == "__main__":
    # Run tests
    test_sieve()
    
    # Run demonstration
    run_demonstration(steps=50, visualize=True)
