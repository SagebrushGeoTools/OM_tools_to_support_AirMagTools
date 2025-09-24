from setuptools import setup, find_packages

setup(
    name="AirMagTools",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "click",
        "geopandas",
        "contextily",
        "scipy",
        "pyproj"
    ],
    include_package_data=True,
    package_data={
        "AirMagTools": ["*.csv"],
    },
    entry_points={
        'console_scripts': [
            'AirMagTools=AirMagTools.pipeline:main',
        ],
        'mag_pipeline.filters': [
            'set_constants = AirMagTools.magfilters:set_constants',
            'diurnal_qc_for_15s_chord = AirMagTools.magfilters:diurnal_qc_for_15s_chord',
            'diurnal_qc_for_60s_chord = AirMagTools.magfilters:diurnal_qc_for_60s_chord',
            'drape_and_speed_qc = AirMagTools.magfilters:drape_and_speed_qc',
            'noise_qc = AirMagTools.magfilters:noise_qc',
            'write_noise_summary = AirMagTools.magfilters:write_noise_summary',
            'write_diurnal_summary = AirMagTools.magfilters:write_diurnal_summary',
            'write_drape_summary = AirMagTools.magfilters:write_drape_summary',
            'set_meta = AirMagTools.magfilters:set_meta',
            'lowpass_filter_butterworth = AirMagTools.magfilters:lowpass_filter_butterworth',
            'highpass_filter_butterworth = AirMagTools.magfilters:highpass_filter_butterworth',
            'bandpass_filter_butterworth = AirMagTools.magfilters:bandpass_filter_butterworth',
            'downline_distance = AirMagTools.magfilters:downline_distance',
            'elevation = AirMagTools.magfilters:elevation',
            'surface_error = AirMagTools.magfilters:surface_error',
        ],        
    },
)
