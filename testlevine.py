 plt.axhline(0, color='gray', ls='--', lw=0.5)
        plt.axvline(0, color='gray', ls='--', lw=0.5)
        plt.legend(loc='upper right')
        plt.grid(alpha=0.3)
        plt.axis('equal')
        plt.title(f"Levine et al. HI Spiral Arms ({coord_system} Coordinates)")
        plt.show()

# Usage Example
if __name__ == "__main__":
    spiral_model = LevineSpiral(R0=8.5)
    
    # Plot in Heliocentric coordinates (default)
    spiral_model.plot_arms(coord_system='HC', R_max=25)
    
    # Plot in Galactocentric coordinates
    spiral_model.plot_arms(coord_system='GC', R_max=25)
