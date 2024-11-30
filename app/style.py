CSS_STYLE = """
    <style>
    
    /* Disable status widget */
    [data-testid="stStatusWidget"] {
        visibility: hidden;
    }
    
    /* Container styling for the game board */
    [data-testid="column"] {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0 !important;
    }
    [data-testid="stMainBlockContainer"] {
        padding-top: 2rem !important;
    }
    /* Game board container size limit */
    [data-testid="stVerticalBlock"] {
        max-width: 500px !important;
        margin: 0 auto !important;
    }

    /* Make buttons square and responsive */
    [data-testid="stBaseButton"],  [data-testid="stBaseButton-secondary"], [data-testid="stTooltipHoverTarget"] {
        aspect-ratio: 1 !important;
        width: 100% !important;
        height: auto !important;
        font-size: calc(100px + 2vw) !important;
        margin: 2px !important;
        border-radius: 8px !important;
        padding: 0 !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        color: black !important;
    }

    /* Ensure columns are displayed correctly on mobile devices */
    [data-testid="stColumn"] {
        width: calc(33.3333% - 1rem) !important;
        flex: 1 1 calc(33.3333% - 1rem) !important;
        min-width: calc(33% - 1rem) !important;
    }
    
    /* Improve segmented control */
    [data-testid="stBaseButton-segmented_controlActive"], [data-testid="stBaseButton-segmented_control"] {
        padding: 1.5rem 1rem !important;
    }
    [data-testid="stBaseButton-primary"] {
        padding: 0rem 0rem !important;
    }
    </style> 
    """
