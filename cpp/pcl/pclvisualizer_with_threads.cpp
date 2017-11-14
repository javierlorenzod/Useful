/* Extracted from https://stackoverflow.com/a/9012240/4482080
It is a not working example that I need to rewrite. However it helps to find a way
of using PCLVisualizer from Point Cloud Library (PCL) in another thread if you don't
remember/know pretty much about multithreading programming */
bool update;
boost::mutex updateModelMutex;
pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZRGB>);

void visualize()  
{  
    // prepare visualizer named "viewer"
    while (!viewer->wasStopped ())
    {
        viewer->spinOnce (100);
        // Get lock on the boolean update and check if cloud was updated
        boost::mutex::scoped_lock updateLock(updateModelMutex);
        if(update)
        {
            if(!viewer->updatePointCloud(cloud, "sample cloud"))
              viewer->addPointCloud(cloud, colorHandler, "sample cloud");
            update = false;
        }
        updateLock.unlock();
    }   
}  

int main()
{
    //Start visualizer thread
    boost::thread workerThread(visualize); 
    while(notFinishedProcessing)
    {
       boost::mutex::scoped_lock updateLock(updateModelMutex);
      update = true;
      // do processing on cloud
       updateLock.unlock();
    }
    workerThread.join();  
}
