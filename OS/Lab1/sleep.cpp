#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>
#include <condition_variable>

std::mutex mtx;
std::condition_variable cv;
bool flag = false;

void producer() {
    std::this_thread::sleep_for(std::chrono::seconds(2));
    std::cout << "Producer: Producing item...\n";
    
    {
        std::lock_guard<std::mutex> lock(mtx);
        flag = true;
    }
    
    std::cout << "Producer: Waking up consumer\n";
    cv.notify_one(); // Wake up the consumer
}

void consumer() {
    std::unique_lock<std::mutex> lock(mtx);
    
    // Wait until flag becomes true
    cv.wait(lock, []{ return flag; });
    
    std::cout << "Consumer: Consuming item\n";
}

int main() {
    std::thread t1(consumer);
    std::thread t2(producer);
    
    t1.join();
    t2.join();
    
    return 0;
}