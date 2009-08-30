# file: transpotools.py
# @date: August, 4, 2009
# this file builds the QGIS Menu and connects the menu items to the proper functions and methods

from PyQt4.QtCore import *
from PyQt4.QtGui import *
# import resources
from qgis.core import *

class transpoToolsPlugin:
    def __init__( self, iface ):
        self.iface = iface

    def initGui( self ):
        self.menu = QMenu()
        self.menu.setTitle( QCoreApplication.translate( "transpoTools", "&Transportation" ) )

        # Geoprocessing Menu
        self.geoProcessingMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Geoprocessing" ) )
        self.genBuffer = QAction( QCoreApplication.translate( "transpoTools", "Generate a buffer layer" ), self.iface.mainWindow() )
        self.genCentroid = QAction( QCoreApplication.translate( "transpoTools", "Generate centroids" ), self.iface.mainWindow() )
        self.genCentroidConnectors = QAction( QCoreApplication.translate( "transpoTools", "Generate centroid connectors" ), self.iface.mainWindow() )
        self.intersectionDesigner = QAction( QCoreApplication.translate( "transpoTools", "Intersection designer" ), self.iface.mainWindow() )
        self.roadProperties = QAction( QCoreApplication.translate( "transpoTools", "Road properties" ), self.iface.mainWindow() )
        self.statistics = QAction( QCoreApplication.translate( "transpoTools", "Statitstics" ), self.iface.mainWindow() )
        self.genTravelTime = QAction( QCoreApplication.translate( "transpoTools", "Generate Travel Time Matrix" ), self.iface.mainWindow() )
        self.genSpeedColumn = QAction( QCoreApplication.translate( "transpoTools", "Generate Speed Column" ), self.iface.mainWindow() )
        self.geoProcessingMenu.addActions( [self.genBuffer, self.genCentroid, self.genCentroidConnectors, self.menu.addSeparator(),
                                            self.intersectionDesigner, self.roadProperties, self.statistics, self.genTravelTime,
                                            self.genSpeedColumn] )

        # travel QRM menu 
        self.travelQRMMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Travel Modeling QRM - NCHRP 365" ) )
        self.dataSetup = QAction( QCoreApplication.translate( "transpoTools", "Step 0: Data setup (CLICK ME FIRST!)" ), self.iface.mainWindow() )
        self.tripGeneration = QAction( QCoreApplication.translate( "transpoTools", "Step 1: Trip generation" ), self.iface.mainWindow() )
        self.tripDistribution = QAction( QCoreApplication.translate( "transpoTools", "Step 2: Trip distribution" ), self.iface.mainWindow() )
        self.modeChoiceAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Step 3: Mode choice" ), self.iface.mainWindow() )
        self.trafficAssignment = QAction( QCoreApplication.translate( "transpoTools", "Step 4: Traffic assignment" ) , self.iface.mainWindow() )
        self.externalTravelEstimation = QAction( QCoreApplication.translate( "transpoTools", "Estimate external travel" ), self.iface.mainWindow() )
        self.automobileOccupancy = QAction( QCoreApplication.translate( "transpoTools", "Automobile occupancy" ), self.iface.mainWindow() )
        self.timeOfDay = QAction( QCoreApplication.translate( "transpoTools", "Time of Day analysis" ), self.iface.mainWindow() )
        self.capacityAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Capacity Analysis" ) , self.iface.mainWindow() )
        self.highwaySpacing = QAction( QCoreApplication.translate( "transpoTools", "Highway Spacing" ) , self.iface.mainWindow() )
        self.travelQRMMenu.addActions( [ self.dataSetup, self.tripGeneration, self.tripDistribution, self.modeChoiceAnalysis, self.trafficAssignment,
                                        self.externalTravelEstimation, self.automobileOccupancy, self.timeOfDay, self.capacityAnalysis, self.highwaySpacing ] )

        # travel ITE Menu
        self.travelITEMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Travel Modeling ITE - ITE Manual 2004" ) )
        self.dataSetup = QAction( QCoreApplication.translate( "transpoTools", "Step 0: Data setup (CLICK ME FIRST!)" ), self.iface.mainWindow() )
        self.travelITEMenu.addActions( [self.dataSetup] )

        # Transit Analysis Menu
        self.transitAnalysisMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Transit Analysis (TCRP - Report 100)" ) )
        self.transitAnalysisDataSetup = QAction( QCoreApplication.translate( "transpoTools", "Data Setup (CLICK ME FIRST!)" ), self.iface.mainWindow() )
        self.transitAvailability = QAction( QCoreApplication.translate( "transpoTools", "Availability Analysis" ), self.iface.mainWindow() )
        self.transitComfort = QAction( QCoreApplication.translate( "transpoTools", "Transit comfort" ), self.iface.mainWindow() )
        self.qualityOfService = QAction( QCoreApplication.translate( "transpoTools", "Generate Transit Supportive Areas" ), self.iface.mainWindow() )
        self.demandResponsiveTransit = QAction( QCoreApplication.translate( "transpoTools", "Demand Responsive Transit" ), self.iface.mainWindow() )
        self.lightRailAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Light Rail Analysis" ), self.iface.mainWindow() )
        self.busAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Bus Analysis" ), self.iface.mainWindow() )
        self.gradeSeperation = QAction( QCoreApplication.translate( "transpoTools", "Grade Seperation between Modes" ), self.iface.mainWindow() )
        self.dedicatedBusLanes = QAction( QCoreApplication.translate( "transpoTools", "Dedidcated Bus Lanes" ), self.iface.mainWindow() )
        self.mixedTraffic = QAction( QCoreApplication.translate( "transpoTools", "Mixed Traffic Analysis" ), self.iface.mainWindow() )
        self.transitAnalysisMenu.addActions( [self.transitAnalysisDataSetup, self.transitAvailability, self.transitComfort,
                                              self.qualityOfService, self.demandResponsiveTransit, self.lightRailAnalysis,
                                              self.busAnalysis, self.dedicatedBusLanes, self.mixedTraffic] )

        # Transit Designer Menu
        self.transitDesignMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Transit Designer" ) )
        self.routeDesigner = QAction( QCoreApplication.translate( "transpoTools", "Route Designer" ), self.iface.mainWindow() )
        self.fareEstimator = QAction( QCoreApplication.translate( "transpoTools", "Fare Estimator" ), self.iface.mainWindow() )
        self.busStopLocator = QAction( QCoreApplication.translate( "transpoTools", "Generate Bus Stops" ), self.iface.mainWindow() )
        self.scheduleCreator = QAction( QCoreApplication.translate( "transpoTools", "Scheudle Creator" ), self.iface.mainWindow() )
        self.transitDesignMenu.addActions( [self.routeDesigner, self.fareEstimator, self.busStopLocator, self.scheduleCreator] )

        # Operations Menu
        self.operationsMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Operations" ) )
        self.tsp = QAction( QCoreApplication.translate( "transpoTools", "Travel Salesman Problem" ), self.iface.mainWindow() )
        self.nearestInsertion = QAction( QCoreApplication.translate( "transpoTools", "Nearest Insertion" ), self.iface.mainWindow() )
        self.chinesePostman = QAction( QCoreApplication.translate( "transpoTools", "Chinese Postman PRoblem" ), self.iface.mainWindow() )
        self.garbageCollection = QAction( QCoreApplication.translate( "transpoTools", "Garbage Collection Problem" ), self.iface.mainWindow() )
        self.operationsMenu.addActions( [self.tsp, self.nearestInsertion, self.chinesePostman, self.garbageCollection] )

        # Traffic Analysis Menu
        self.trafficAnalysisMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Traffic Analysis" ) )
        self.trafficLightWarrant = QAction( QCoreApplication.translate( "transpoTools", "Traffic Light Warrant" ), self.iface.mainWindow() )
        self.controlledIntersectionWarrant = QAction( QCoreApplication.translate( "transpoTools", "Controlled Intersection Warrant" ), self.iface.mainWindow() )
        self.trafficImpactAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Traffic Impact Analysis" ), self.iface.mainWindow() )
        self.capacityAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Capacity Analysis" ), self.iface.mainWindow() )
        self.roadLOS = QAction( QCoreApplication.translate( "transpoTools", "Road Level of Service" ), self.iface.mainWindow() )
        self.intersectionLOS = QAction( QCoreApplication.translate( "transpoTools", "Intersection Level of Service" ), self.iface.mainWindow() )
        self.trafficSignalAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Traffic Signal Analysis" ), self.iface.mainWindow() )
        self.trafficAnalysisMenu.addActions( [self.trafficLightWarrant, self.controlledIntersectionWarrant, self.trafficImpactAnalysis,
                                             self.capacityAnalysis, self.roadLOS, self.intersectionLOS, self.trafficSignalAnalysis] )

        # Transportation Safety Menu
        self.safetyAnalysisMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Safety Analysis" ) )
        self.collisionPredictionModel = QAction( QCoreApplication.translate( "transpoTools", "Collision Prediction Model" ), self.iface.mainWindow() )
        self.collisionDiagram = QAction( QCoreApplication.translate( "transpoTools", "Create a Collision Diagram" ), self.iface.mainWindow() )
        self.lineOfSightAnalysis = QAction( QCoreApplication.translate( "transpoTools", "Line of Sight Issues" ), self.iface.mainWindow() )
        self.safetyAnalysisMenu.addActions( [self.collisionPredictionModel, self.collisionDiagram, self.lineOfSightAnalysis ] )

        # Environmental Analysis Menu
        self.environmentalAnalysisMenu = QMenu( QCoreApplication.translate( "transpoTools", "&Environmental Analysis" ) )
        self.mobile6 = QAction( QCoreApplication.translate( "transpoTools", "Mobile 6 Analysis..." ), self.iface.mainWindow() )
        self.summit = QAction( QCoreApplication.translate( "transpoTools", "SUMMIT..." ), self.iface.mainWindow() )
        self.environmentalAnalysisMenu .addActions( [self.mobile6, self.summit] )

        # PostGIS Menu
        self.postGIS = QAction( QCoreApplication.translate( "transpoTools", "Connect to PostGIS" ), self.iface.mainWindow() )

        # about tranpoTools
        self.aboutTranspoTools = QAction( QCoreApplication.translate( "transpoTools", "About TranspoTools" ), self.iface.mainWindow() )

        # Add all submenus to main menu
        self.menu.addMenu( self.geoProcessingMenu )
        self.menu.addSeparator()
        self.menu.addMenu( self.travelQRMMenu )
        self.menu.addMenu( self.travelITEMenu )
        self.menu.addSeparator()
        self.menu.addMenu( self.operationsMenu )
        self.menu.addMenu( self.trafficAnalysisMenu )
        self.menu.addSeparator()
        self.menu.addMenu( self.safetyAnalysisMenu )
        self.menu.addMenu( self.environmentalAnalysisMenu )
        self.menu.addSeparator()
        self.menu.addMenu( self.transitAnalysisMenu )
        self.menu.addMenu( self.transitDesignMenu )
        self.menu.addSeparator()
        self.menu.addAction( self.postGIS )
        self.menu.addAction( self.aboutTranspoTools )

        menuBar = self.iface.mainWindow().menuBar()
        actions = menuBar.actions()
        lastAction = actions[ len( actions ) - 1 ]
        menuBar.insertMenu( lastAction, self.menu )

    def unload( self ):
        pass

