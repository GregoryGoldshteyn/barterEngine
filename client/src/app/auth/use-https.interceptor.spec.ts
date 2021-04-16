import { TestBed } from '@angular/core/testing';

import { UseHttpsInterceptor } from './use-https.interceptor';

describe('UseHttpsInterceptor', () => {
  beforeEach(() => TestBed.configureTestingModule({
    providers: [
      UseHttpsInterceptor
      ]
  }));

  it('should be created', () => {
    const interceptor: UseHttpsInterceptor = TestBed.inject(UseHttpsInterceptor);
    expect(interceptor).toBeTruthy();
  });
});
